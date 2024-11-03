from app.controller.general_controller import GeneralController
from ..service import vacanci_service

class VacanciController(GeneralController):
    _service = vacanci_service


