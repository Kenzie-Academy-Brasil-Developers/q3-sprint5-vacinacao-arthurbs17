from datetime import datetime
from sqlalchemy import Column, String, DateTime
from app.configs.database import db 
from dataclasses import dataclass

@dataclass
class VaccineCardModel(db.Model):
    cpf: str
    name: str
    first_shot_date: datetime
    second_shot_date: datetime
    vaccine_name: str
    health_unit_name: str

    __tablename__ = "vaccine_cards"

    cpf = Column(String(11), primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)