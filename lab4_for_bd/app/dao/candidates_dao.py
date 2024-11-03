from app.dao.general_dao import GeneralDAO
from app.domain import Candidates


class CandidatesDAO(GeneralDAO):
    _domain_type = Candidates
