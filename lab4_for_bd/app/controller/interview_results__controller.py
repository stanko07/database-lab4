from app.controller.general_controller import GeneralController
from ..service import interview_results_service

class InterviewResultsController(GeneralController):
    _service = interview_results_service
