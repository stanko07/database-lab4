from app.service.general_service import GeneralService
from app.dao import company_dao

class CompanyService(GeneralService):
    _dao = company_dao



