from app.controller.general_controller import GeneralController
from ..service import contact_person_service

class ContactPersonController(GeneralController):
    _service = contact_person_service
