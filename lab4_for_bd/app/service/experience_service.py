from app.service.general_service import GeneralService
from app.dao import experience_dao

class ExperienceService(GeneralService):
    _dao = experience_dao
