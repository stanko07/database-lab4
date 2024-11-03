from app.service.general_service import GeneralService
from app.dao import candidate_have_skills_dao

class CandidateHaveSkillsService(GeneralService):
    _dao = candidate_have_skills_dao
