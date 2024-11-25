from flask import Flask

from .error_handler import err_handler_bp
from .candidate_have_skills_route import candidate_have_skills_bp
from .candidates_route import candidates_controller_bp
from .company_route import company_bp
from .contact_person_route import contact_person_bp
from .experience_route import experience_bp
from .interview_results_route import interview_results_bp
from .interviews_route import interviews_bp
from .project_route import project_bp
from .skills_route import skills_bp
from .vacancii_route import vacancii_bp 
from .education_route import education_controller_bp


def register_routes(app: Flask) -> None:
    app.register_blueprint(err_handler_bp)
    
    app.register_blueprint(candidate_have_skills_bp)
    app.register_blueprint(candidates_controller_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(contact_person_bp)
    app.register_blueprint(experience_bp)
    app.register_blueprint(interview_results_bp)
    app.register_blueprint(interviews_bp)
    app.register_blueprint(project_bp)
    app.register_blueprint(skills_bp)
    app.register_blueprint(vacancii_bp)
    app.register_blueprint(education_controller_bp)

