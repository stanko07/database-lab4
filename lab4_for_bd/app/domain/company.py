from __future__ import annotations
from typing import Dict, Any
from app.database import db

class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(45))

    vacancies = db.relationship('Vacanci', backref='company', lazy=True)
    interviews = db.relationship('Interview', backref='company', lazy=True)
    experiences = db.relationship('Experience', backref='company', lazy=True)

    def __repr__(self) -> str:
        return f"Company({self.id}, 'name={self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Company:
        return Company(
            name=dto_dict.get('name'),
            address=dto_dict.get('address')
        )