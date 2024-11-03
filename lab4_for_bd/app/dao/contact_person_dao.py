from app.dao.general_dao import GeneralDAO
from app.domain import ContactPerson


class ContactPersonDAO(GeneralDAO):
    _domain_type = ContactPerson
