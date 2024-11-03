from app.service.general_service import GeneralService
from app.dao import vacanci_dao

class VacanciService(GeneralService):
    _dao = vacanci_dao
