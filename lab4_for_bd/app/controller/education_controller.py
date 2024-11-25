from app.controller.general_controller import GeneralController
from ..service import education_service

class EducationController(GeneralController):
    _service = education_service
