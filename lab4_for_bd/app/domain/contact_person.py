from __future__ import annotations
from typing import Dict, Any
from app.database import db

class ContactPerson(db.Model):
    __tablename__ = 'contact_person'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(100), unique=True)
    vacancies = db.relationship('Vacanci', backref='contact_person')


    def __repr__(self) -> str:
        return f"ContactPerson({self.id}, 'name={self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        vacancies = [vacanci.put_into_dto() for vacanci in self.vacancies]
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'vacancies' : vacancies if vacancies else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ContactPerson:
        return ContactPerson(
            name=dto_dict.get('name'),
            phone=dto_dict.get('phone'),
            email=dto_dict.get('email')
        )