from app.dao.general_dao import GeneralDAO
from app.domain import Company


class CompanyDAO(GeneralDAO):
    _domain_type = Company
