from app.dao.general_dao import GeneralDAO
from app.domain import InterviewResult


class InterviewResultsDAO(GeneralDAO):
    _domain_type = InterviewResult
