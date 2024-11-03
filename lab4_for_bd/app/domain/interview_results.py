from __future__ import annotations
from typing import Dict, Any
from app.database import db
from sqlalchemy import Enum

class InterviewResult(db.Model):
    __tablename__ = 'Interview_Results'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rating = db.Column(Enum('low', 'medium', 'high', name='rating_enum'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=True)
    interview_id = db.Column(db.Integer, db.ForeignKey('Interviews.id'), nullable=True)

    def __repr__(self) -> str:
        return f"InterviewResult({self.id}, 'rating={self.rating}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'rating': self.rating,
            'candidate_id': self.candidate_id,
            'interview_id': self.interview_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> InterviewResult:
        return InterviewResult(
            rating=dto_dict.get('rating'),
            candidate_id=dto_dict.get('candidate_id'),
            interview_id=dto_dict.get('interview_id')
        )