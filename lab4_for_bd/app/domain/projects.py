from __future__ import annotations
from typing import Dict, Any
from app.database import db

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(50))
    vacancies = db.relationship('Vacanci', backref='projects')

    def __repr__(self) -> str:
        return f"Project({self.id}, 'name={self.name}',capacity='{self.capacity}')"

    def put_into_dto(self) -> Dict[str, Any]:
        vacancies = [vacanci.put_into_dto() for vacanci in self.vacancies]
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'capacity': self.capacity,
            'vacancies' : vacancies if vacancies else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Project:
        return Project(
            name=dto_dict.get('name'),
            description=dto_dict.get('description'),
            capacity=dto_dict.get('capacity')
        )
    
def insert_projects(n):
    projects = [
        Project(
            name=f"No-name{i}",
            description="Unknown",
            capacity= i + 1
        )
        for i in range(n)
    ]

    try:
        db.session.bulk_save_objects(projects)
        db.session.commit()
        return projects
    except Exception:
        db.session.rollback()
        return -1
    



def get_through_capacity(stat_type):
    if stat_type == 'MAX':
        result = db.session.query(db.func.max(Project.capacity)).scalar()
        return result
    elif stat_type == 'MIN':
        result = db.session.query(db.func.min(Project.capacity)).scalar()
        return result
    elif stat_type == 'SUM':
        result = db.session.query(db.func.sum(Project.capacity)).scalar()
        return result
    elif stat_type == 'AVG':
        result = db.session.query(db.func.avg(Project.capacity)).scalar()
        return result
    else:
        return -1