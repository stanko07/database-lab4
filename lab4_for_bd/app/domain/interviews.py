from __future__ import annotations
from typing import Dict, Any, Optional
from datetime import datetime
from app.database import db
from sqlalchemy import Enum

class Interview(db.Model):
    __tablename__ = 'Interviews'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Date)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=True)

    def __repr__(self) -> str:
        return f"Interview({self.id}, 'date={self.date}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'date': self.date,
            'company_id': self.company_id,
            'candidate_id': self.candidate_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Interview:
        date_str: Optional[str] = dto_dict.get('date')
        date_obj = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z').date() if date_str else None
        return Interview(
            date=date_obj,
            company_id=dto_dict.get('company_id'),
            candidate_id=dto_dict.get('candidate_id')
        )