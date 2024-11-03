from __future__ import annotations
from typing import Dict, Any
from app.database import db

class Vacanci(db.Model):
    __tablename__ = 'vacanci'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(45), nullable=False)
    description = db.Column(db.Text, nullable=True)
    contact_person_id = db.Column(db.Integer, db.ForeignKey('contact_person.id'), nullable=False)
    projects_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)


    def __repr__(self) -> str:
        return f"Vacanci({self.id}, title={self.title})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'contact_person_id': self.contact_person_id,
            'projects_id': self.projects_id,
            'company_id': self.company_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Vacanci:
        return Vacanci(
            title=dto_dict.get('title'),
            description=dto_dict.get('description'),
            contact_person_id=dto_dict.get('contact_person_id'),
            projects_id=dto_dict.get('projects_id'),
            company_id=dto_dict.get('company_id')
        )
