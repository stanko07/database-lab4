from app.service.general_service import GeneralService
from app.dao import candidates_dao

class CandidatesService(GeneralService):
    _dao = candidates_dao
