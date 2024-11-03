from app.controller.general_controller import GeneralController
from ..service import candidates_service

class CandidatesController(GeneralController):
    _service = candidates_service

