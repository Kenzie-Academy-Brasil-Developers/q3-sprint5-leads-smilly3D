from datetime import datetime
from http import HTTPStatus
import re
from flask import jsonify, request
from sqlalchemy.orm.session import Session

from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound

from app.models.leads_models import LeadsModel
from app.configs.database import db
from app.services.decorator import verify_entry_key


def validNumber(phone_nuber):
    pattern = re.compile("^\\([\d]{2}\\)[\d]{5}-[\d]{4}$", re.IGNORECASE)
    return pattern.match(phone_nuber) is not None

def create_lead():

    data = request.get_json()

    if not validNumber(data["phone"]):
        return {"error": "Telefone obrigatoriamente no formato (xx)xxxxx-xxxx"}, HTTPStatus.BAD_REQUEST
    
    try:
        lead = LeadsModel(**data)

        db.session.add(lead)
        db.session.commit()
    except IntegrityError:
        return {"error": "E-mail e telefone único"},HTTPStatus.BAD_REQUEST

    return jsonify(lead)


def get_lead():

    session: Session = db.session
    base_query = session.query(LeadsModel)

    leads = base_query.order_by(LeadsModel.visits).all()

    if not leads:
        return {"error": "Nenhum dado encontrado."}, HTTPStatus.NOT_FOUND

    return jsonify(leads)

@verify_entry_key("email")
def patch_lead():
    session: Session = db.session
    base_query = session.query(LeadsModel)

    data = request.get_json()
    lead_email = data["email"]
 

    try:
        lead = base_query.filter_by(email= lead_email).first_or_404(description="Nenhum dado encontrado")
        lead.last_visit = datetime.now()
        lead.visits += 1

        for key, value in data.items():
            setattr(lead, key, value)

        session.add(lead)
        session.commit()

    except NotFound as e:
        return {"error": e.description}, HTTPStatus.NOT_FOUND

    return "", HTTPStatus.NO_CONTENT


@verify_entry_key("email")
def delete_lead():
    session: Session = db.session
    base_query = session.query(LeadsModel)

    data = request.get_json()
    lead_email = data["email"]

    try:
        lead = base_query.filter_by(email= lead_email).first_or_404(description="Nenhum dado encontrado")

        session.delete(lead)
        session.commit()

    except NotFound as e:
        return {"error": e.description}, HTTPStatus.NOT_FOUND

    return "", HTTPStatus.NO_CONTENT


 

