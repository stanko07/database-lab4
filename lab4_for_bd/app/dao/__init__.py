from .candidate_have_skills_dao import CandidateHaveSkillsDAO
from .candidates_dao import CandidatesDAO
from .company_dao import CompanyDAO
from .contact_person_dao import ContactPersonDAO
from .experience_dao import ExperienceDAO
from .general_dao import GeneralDAO
from .interview_results_dao import InterviewResultsDAO
from .interviews_dao import InterviewsDAO
from .projects_dao import ProjectsDAO
from .skills_dao import SkillsDAO
from .vacanci_dao import VacanciDAO
from .education_dao import EducationDAO


candidate_have_skills_dao = CandidateHaveSkillsDAO()
candidates_dao = CandidatesDAO()
company_dao = CompanyDAO()
contact_person_dao = ContactPersonDAO()
experience_dao = ExperienceDAO()
general_dao = GeneralDAO()
interview_results_dao = InterviewResultsDAO()
interviews_dao = InterviewsDAO()
projects_dao = ProjectsDAO()
skills_dao = SkillsDAO()
vacanci_dao = VacanciDAO()
education_dao = EducationDAO()
