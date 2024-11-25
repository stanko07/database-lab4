from __future__ import annotations
from typing import Dict, Any, Optional
from app.database import db
from sqlalchemy import event, select

class Education(db.Model):
    __tablename__ = 'education'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.id'), nullable=False)
    institution_name = db.Column(db.String(100), nullable=False)
    degree = db.Column(db.String(50), nullable=False)
    graduation_year = db.Column(db.Integer, nullable=False)
    cathedra = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"Education(id={self.id}, institution_name='{self.institution_name}', " \
            f"degree='{self.degree}', graduation_year={self.graduation_year}, cathedra={self.cathedra})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'candidate_id': self.candidate_id, 
            'institution_name': self.institution_name,
            'degree': self.degree,
            'graduation_year': self.graduation_year,
            'cathedra': self.cathedra
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Education:
        return Education(
            candidate_id=dto_dict.get('candidate_id'),  # Правильний атрибут
            institution_name=dto_dict.get('institution_name'),
            degree=dto_dict.get('degree'),
            graduation_year=dto_dict.get('graduation_year'),
            cathedra=dto_dict.get('cathedra')
        )


@event.listens_for(Education, "before_insert")
def check_team_from_to(mapper, connection, target):
    candidate_table = db.Table('candidates', db.metadata, autoload_with=db.engine)

    candidate_exists = connection.execute(
        select(candidate_table.c.id).where(candidate_table.c.id == target.candidate_id) 
    ).first()

    if not candidate_exists:
        raise ValueError(f"Candidate with id {target.candidate_id} does not exist in candidates table.")
