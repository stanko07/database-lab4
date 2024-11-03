from app.controller.general_controller import GeneralController
from ..service import candidate_have_skills_service

class CandidateHaveSkillsController(GeneralController):
    _service = candidate_have_skills_service
