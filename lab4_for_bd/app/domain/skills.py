from __future__ import annotations
from typing import Dict, Any
from app.database import db

class Skill(db.Model):
    __tablename__ = 'Skills'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    skills_candidate = db.relationship('Candidates', secondary="Candidates_has_Skills", back_populates="candidate_skills")


    def __repr__(self) -> str:
        return f"Skill({self.id}, 'name={self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Skill:
        return Skill(
            name=dto_dict.get('name')
        )