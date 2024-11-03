from app.controller.general_controller import GeneralController
from ..service import skills_service

class SkillsController(GeneralController):
    _service = skills_service
