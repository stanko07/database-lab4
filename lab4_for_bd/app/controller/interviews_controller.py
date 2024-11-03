from app.controller.general_controller import GeneralController
from ..service import interviews_service

class InterviewsController(GeneralController):
    _service = interviews_service
