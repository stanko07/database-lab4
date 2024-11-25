from __future__ import annotations
from typing import Dict, Any
from app.database import db

class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(45))

    vacancies = db.relationship('Vacanci', backref='companies')
    interviews = db.relationship('Interview', backref='companies')
    experiences = db.relationship('Experience', backref='companies')

    def __repr__(self) -> str:
        return f"Company({self.id}, 'name={self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        interviews = [interview.put_into_dto() for interview in self.interviews]
        vacancies = [vacanci.put_into_dto() for vacanci in self.vacancies]
        experiences = [experience.put_into_dto() for experience in self.experiences]
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'interviews' : interviews if interviews  else None,
            'vacancies' : vacancies if vacancies else None,
            'experiences': experiences if experiences else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Company:
        return Company(
            name=dto_dict.get('name'),
            address=dto_dict.get('address')
        )
    

def insert_company(name, address) -> Company:
    new_company = Company(name=name, address=address)
    db.session.add(new_company)
    db.session.commit()
    return new_company