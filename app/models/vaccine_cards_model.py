from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, Date, DateTime
from app.configs.database import db
from dataclasses import dataclass


@dataclass
class VaccineCard(db.Model):

    __tablename__ = "vaccine_cards"

    cpf: str = Column(String, primary_key=True)
    name: str = Column(String, nullable=False)
    first_shot_date: str = Column(DateTime, default=datetime.now())
    second_shot_date: str = Column(DateTime, default=(datetime.today() + timedelta(days=+90)))
    vaccine_name: str = Column(String, nullable=False)
    health_unit_name: str = Column(String)

    def __repr__(self):
        return f"<[{self.cpf}]{self.name}>"

    def serializer(self):
        return {
            "cpf": self.cpf,
            "name": self.name,
            "first_shot_date": self.first_shot_date,
            "second_shot_date": self.second_shot_date,
            "vaccine_name": self.vaccine_name,
            "health_unit_name": self.health_unit_name,
        }
