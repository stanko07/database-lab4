from __future__ import annotations
from typing import Dict, Any
from app.database import db
from datetime import datetime, date

class Experience(db.Model):
    __tablename__ = 'Experience'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_title = db.Column(db.String(45))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    company_id = db.Column(db.Integer, db.ForeignKey('Companies.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('Candidates.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Experience(id='{self.id}', 'job_title={self.job_title}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'job_title': self.job_title,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'company_id': self.company_id,
            'candidate_id': self.candidate_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Experience:
        
        def parse_date(date_str: str) -> date:
            if not date_str:
                return None
            try:
                return datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                try:
                    return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S GMT').date()
                except ValueError:
                    raise ValueError(f"Unsupported date format: {date_str}")

        
        return Experience(
            job_title=dto_dict.get('job_title'),
            start_date=parse_date(dto_dict.get('start_date')),
            end_date=parse_date(dto_dict.get('end_date')),
            company_id=dto_dict.get('company_id'),
            candidate_id=dto_dict.get('candidate_id')
        )
