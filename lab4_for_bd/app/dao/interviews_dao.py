from app.dao.general_dao import GeneralDAO
from app.domain import Interview


class InterviewsDAO(GeneralDAO):
    _domain_type = Interview
