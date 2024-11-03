from app.controller.general_controller import GeneralController
from ..service import projects_service

class ProjectsController(GeneralController):
    _service = projects_service
