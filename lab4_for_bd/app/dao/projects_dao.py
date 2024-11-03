from app.dao.general_dao import GeneralDAO
from app.domain import Project


class ProjectsDAO(GeneralDAO):
    _domain_type = Project
