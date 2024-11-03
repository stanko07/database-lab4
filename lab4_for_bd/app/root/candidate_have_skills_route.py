from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller import candidate_have_skills_controller
from ..domain.candidate_have_skills import CandidateHaveSkills

candidate_have_skills_bp = Blueprint('candidate_have_skills', __name__, url_prefix='/candidate_have_skills')


@candidate_have_skills_bp.route('', methods=['GET'])
def get_all_goals() -> Response:
    return make_response(jsonify(candidate_have_skills_controller.find_all()), HTTPStatus.OK)


@candidate_have_skills_bp.route('', methods=['POST'])
def create_goal() -> Response:
    content = request.get_json()
    candidate_have_skills = CandidateHaveSkills.create_from_dto(content)
    candidate_have_skills_controller.create(candidate_have_skills)
    return make_response(jsonify(candidate_have_skills.put_into_dto()), HTTPStatus.CREATED)


@candidate_have_skills_bp.route('/<int:candidate_have_skills_id>', methods=['GET'])
def get_goal(candidate_have_skills_id: int) -> Response:
    return make_response(jsonify(candidate_have_skills_controller.find_by_id(candidate_have_skills_id)), HTTPStatus.OK)


@candidate_have_skills_bp.route('/<int:candidate_have_skills_id>', methods=['PUT'])
def update_goal(candidate_have_skills_id: int) -> Response:
    content = request.get_json()
    candidate_have_skills = CandidateHaveSkills.create_from_dto(content)
    candidate_have_skills_controller.update(candidate_have_skills_id, candidate_have_skills)
    return make_response("Goal updated", HTTPStatus.OK)


@candidate_have_skills_bp.route('/<int:candidate_have_skills_id>', methods=['PATCH'])
def patch_goal(candidate_have_skills_id: int) -> Response:
    content = request.get_json()
    candidate_have_skills_controller.patch(candidate_have_skills_id, content)
    return make_response("Goal updated", HTTPStatus.OK)


@candidate_have_skills_bp.route('/<int:candidate_have_skills_id>', methods=['DELETE'])
def delete_goal(candidate_have_skills_id: int) -> Response:
    candidate_have_skills_controller.delete(candidate_have_skills_id)
    return make_response("Goal deleted", HTTPStatus.OK)
