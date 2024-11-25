from app.dao.general_dao import GeneralDAO
from app.domain import Education


class EducationDAO(GeneralDAO):
    _domain_type = Education
