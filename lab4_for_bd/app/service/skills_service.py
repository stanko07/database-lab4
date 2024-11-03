from app.service.general_service import GeneralService
from app.dao import skills_dao

class SkillsService(GeneralService):
    _dao = skills_dao
