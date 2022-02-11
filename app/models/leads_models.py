from dataclasses import dataclass
from sqlalchemy import Column, DateTime, String, Integer
from datetime import datetime

from app.configs.database import db

@dataclass
class LeadsModel(db.Model):
    name: str
    email: str
    phone: str
    creation_date: str
    last_visit: str
    visits: str

    __tablename__ = "leads"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    creation_date = Column(DateTime, default=datetime.now().strftime("%D %H:%M:%S"))
    last_visit = Column(DateTime, default=datetime.now().strftime("%D %H:%M:%S"))
    visits = Column(Integer, default=1)

    
