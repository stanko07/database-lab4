from app.controller.general_controller import GeneralController
from ..service import experience_service

class ExperienceController(GeneralController):
    _service = experience_service
