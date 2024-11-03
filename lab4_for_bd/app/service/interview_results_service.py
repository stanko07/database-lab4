from app.service.general_service import GeneralService
from app.dao import interview_results_dao

class InterviewResultsService(GeneralService):
    _dao = interview_results_dao
