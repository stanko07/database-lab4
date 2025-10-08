from __future__ import annotations
from typing import Dict, Any
from app.database import db

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(50))
    vacancies = db.relationship('Vacanci', backref='projects')

    def __repr__(self) -> str:
        return f"Project({self.id}, 'name={self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        vacancies = [vacanci.put_into_dto() for vacanci in self.vacancies]
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'vacancies' : vacancies if vacancies else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Project:
        return Project(
            name=dto_dict.get('name'),
            description=dto_dict.get('description')
        )