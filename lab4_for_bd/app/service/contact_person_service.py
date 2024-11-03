from app.service.general_service import GeneralService
from app.dao import contact_person_dao

class ContactPersonService(GeneralService):
    _dao = contact_person_dao
