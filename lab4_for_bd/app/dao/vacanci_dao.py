from app.dao.general_dao import GeneralDAO
from app.domain import Vacanci


class VacanciDAO(GeneralDAO):
    _domain_type = Vacanci
