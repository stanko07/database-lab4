from app.dao.general_dao import GeneralDAO
from app.domain import Experience


class ExperienceDAO(GeneralDAO):
    _domain_type = Experience
