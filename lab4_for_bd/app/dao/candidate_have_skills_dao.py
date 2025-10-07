from app.dao.general_dao import GeneralDAO
from app.domain import CandidateHaveSkills

class CandidateHaveSkillsDAO(GeneralDAO):
    _domain_type = CandidateHaveSkills
