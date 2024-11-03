from __future__ import annotations
from typing import Dict, Any
from app.database import db
from sqlalchemy import Enum

class CandidateHaveSkills(db.Model):
    __tablename__ = 'Candidates_has_Skills'

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), primary_key=True)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'), primary_key=True)
    level = db.Column(Enum('junior', 'middle', 'senior'))

    def __repr__(self) -> str:
        return f"CandidateHaveSkills(candidate_id={self.candidate_id}, skill_id={self.skill_id}, level={self.level})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'candidate_id': self.candidate_id,
            'skill_id': self.skill_id,
            'level': self.level
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> CandidateHaveSkills:
        return CandidateHaveSkills(
            candidate_id=dto_dict.get('candidate_id'),
            skill_id=dto_dict.get('skill_id'),
            level=dto_dict.get('level')
        )
