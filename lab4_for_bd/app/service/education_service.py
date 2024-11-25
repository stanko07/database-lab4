from app.service.general_service import GeneralService
from app.dao import education_dao

class EducationService(GeneralService):
    _dao = education_dao
