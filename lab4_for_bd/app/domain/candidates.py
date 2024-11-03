from __future__ import annotations
from typing import Dict, Any
from app.database import db
from sqlalchemy import Enum

# Приклад моделі Candidates
class Candidates(db.Model):
    __tablename__ = 'candidates'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(35), unique=True)

    interviews = db.relationship('Interview', backref='candidate')
    interview_results = db.relationship('InterviewResult', backref='candidate')
    experiences = db.relationship('Experience', backref='candidate')
    skills = db.relationship('CandidateHaveSkills', backref='candidate')

    def __repr__(self) -> str:
        return f"Candidates(id={self.id}, name={self.name}, surname={self.surname})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'phone': self.phone
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Candidates:
        return Candidates(
            name=dto_dict.get('name'),
            surname=dto_dict.get('surname'),
            email=dto_dict.get('email'),
            phone=dto_dict.get('phone')
        )