from app.service.general_service import GeneralService
from app.dao import interviews_dao

class InterviewsService(GeneralService):
    _dao = interviews_dao
