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

    interviews = db.relationship('Interview', backref='candidates')
    interview_results = db.relationship('InterviewResult', backref='candidates')
    experiences = db.relationship('Experience', backref='candidates')
    candidate_skills = db.relationship('Skill', secondary="Candidates_has_Skills", back_populates="skills_candidate")

    def __repr__(self) -> str:
        return f"Candidates(id={self.id}, name={self.name}, surname={self.surname})"

    def put_into_dto(self) -> Dict[str, Any]:
        interviews = [interview.put_into_dto() for interview in self.interviews]
        interview_results = [interview_result.put_into_dto() for interview_result in self.interview_results]
        experiences = [experience.put_into_dto() for experience in self.experiences]
        candidate_skills = [candidate_skill.put_into_dto() for candidate_skill in self.candidate_skills]
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'phone': self.phone,
            'interviews' : interviews if interviews  else None,
            'interview_results' : interview_results if interview_results else None,
            'experiences': experiences if experiences else None,
            'candidate_skills': candidate_skills if candidate_skills else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Candidates:
        return Candidates(
            name=dto_dict.get('name'),
            surname=dto_dict.get('surname'),
            email=dto_dict.get('email'),
            phone=dto_dict.get('phone')
        )