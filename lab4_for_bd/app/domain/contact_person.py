from __future__ import annotations
from typing import Dict, Any
from app.database import db
from random import randint, choice
from time import time
from sqlalchemy import text

class ContactPerson(db.Model):
    __tablename__ = 'contact_person'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(100), unique=True)
    vacancies = db.relationship('Vacanci', backref='contact_person')


    def __repr__(self) -> str:
        return f"ContactPerson({self.id}, 'name={self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        vacancies = [vacanci.put_into_dto() for vacanci in self.vacancies]
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'vacancies' : vacancies if vacancies else None,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ContactPerson:
        return ContactPerson(
            name=dto_dict.get('name'),
            phone=dto_dict.get('phone'),
            email=dto_dict.get('email')
        )
    

def create_dynamic_tables_from_contact_person():
    contacts = ContactPerson.query.all()
    if not contacts:
        return "No group found in the database."

    created_tables = []

    for contact in contacts:
        contact_name = contact.name.replace(" ", "_")
        table_name = f"{contact_name}_{int(time())}"

        column_defs = []
        for i in range(randint(1, 9)):
            column_name = f"column_{i + 1}"
            column_type = choice(["INT", "VARCHAR(255)", "DATE"])
            column_defs.append(f"{column_name} {column_type}")
        column_defs_str = ", ".join(column_defs)

        create_table_sql = text(f"CREATE TABLE {table_name} (id INT PRIMARY KEY AUTO_INCREMENT, {column_defs_str});")

        db.session.execute(create_table_sql)
        db.session.commit()
        created_tables.append(table_name)

    return created_tables
