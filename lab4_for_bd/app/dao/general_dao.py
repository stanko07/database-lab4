from abc import ABC
from typing import List
from sqlalchemy import inspect
from sqlalchemy.orm import Mapper
from app.database import db  # Якщо виникає циклічний імпорт, перенесіть цей імпорт всередину методів


class GeneralDAO(ABC):

    _domain_type = None

    def __init__(self):
        self._session = db.session

    def find_all(self) -> List[object]:
        return self._session.query(self._domain_type).all()

    def find_by_id(self, key: int) -> object:
        return self._session.get(self._domain_type, key)  # Використовуємо get з зазначенням primary key для SQLAlchemy 2.x

    def create(self, obj: object) -> object:
        self._session.add(obj)
        self._session.commit()
        return obj

    def create_all(self, obj_list: List[object]) -> List[object]:
        self._session.add_all(obj_list)
        self._session.commit()
        return obj_list

    def update(self, key: int, in_obj: object) -> None:
        domain_obj = self._session.get(self._domain_type, key)
        mapper: Mapper = inspect(type(in_obj))
        columns = mapper.columns
        for column in columns:
            if not column.primary_key:
                value = getattr(in_obj, column.name)
                setattr(domain_obj, column.name, value)
        self._session.commit()

    def patch(self, key: int, field_name: str, value: object) -> None:
        domain_obj = self._session.get(self._domain_type, key)
        setattr(domain_obj, field_name, value)
        self._session.commit()

    def delete(self, key: int) -> None:
        domain_obj = self._session.get(self._domain_type, key)
        self._session.delete(domain_obj)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise

    def delete_all(self) -> None:
        self._session.query(self._domain_type).delete()
        self._session.commit()
