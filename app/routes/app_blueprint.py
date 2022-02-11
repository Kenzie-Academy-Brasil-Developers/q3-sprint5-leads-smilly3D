from flask import Blueprint
from app.routes.leads_route import bp_leads

bp_api = Blueprint("bp_api", __name__, url_prefix="/api")

#import other routes, bp_api.register(insert routes here)

bp_api.register_blueprint(bp_leads)