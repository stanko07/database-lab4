from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller   import skills_controller
from ..domain.skills import Skill

skills_bp = Blueprint('skills', __name__, url_prefix='/skills')


@skills_bp.route('', methods=['GET'])
def get_all_interview_results() -> Response:
    return make_response(jsonify(skills_controller.find_all()), HTTPStatus.OK)


@skills_bp.route('', methods=['POST'])
def create_interview_result() -> Response:
    content = request.get_json()
    skills = Skill.create_from_dto(content)
    skills_controller.create(skills)
    return make_response(jsonify(skills.put_into_dto()), HTTPStatus.CREATED)


@skills_bp.route('/<int:skills_id>', methods=['GET'])
def get_interview_result(skills_id: int) -> Response:
    return make_response(jsonify(skills_controller.find_by_id(skills_id)), HTTPStatus.OK)


@skills_bp.route('/<int:skills_id>', methods=['PUT'])
def update_interview_result(skills_id: int) -> Response:
    content = request.get_json()
    skills = Skill.create_from_dto(content)
    skills_controller.update(skills_id, skills)
    return make_response("Interview result updated", HTTPStatus.OK)


@skills_bp.route('/<int:skills_id>', methods=['PATCH'])
def patch_interview_result(skills_id: int) -> Response:
    content = request.get_json()
    skills_controller.patch(skills_id, content)
    return make_response("Interview result updated", HTTPStatus.OK)


@skills_bp.route('/<int:skills_id>', methods=['DELETE'])
def delete_interview_result(skills_id: int) -> Response:
    skills_controller.delete(skills_id)
    return make_response("Interview result deleted", HTTPStatus.OK)
