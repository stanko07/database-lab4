from app.service.general_service import GeneralService
from app.dao import projects_dao

class ProjectsService(GeneralService):
    _dao = projects_dao
