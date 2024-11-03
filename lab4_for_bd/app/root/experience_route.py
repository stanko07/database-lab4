from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller   import experience_controller
from ..domain.experience import Experience

experience_bp = Blueprint('experience', __name__, url_prefix='/experience')


@experience_bp.route('', methods=['GET'])
def get_all_experiences() -> Response:
    return make_response(jsonify(experience_controller.find_all()), HTTPStatus.OK)


@experience_bp.route('', methods=['POST'])
def create_experience() -> Response:
    content = request.get_json()
    experience = Experience.create_from_dto(content)
    experience_controller.create(experience)
    return make_response(jsonify(experience.put_into_dto()), HTTPStatus.CREATED)


@experience_bp.route('/<int:experience_id>', methods=['GET'])
def get_experience(experience_id: int) -> Response:
    return make_response(jsonify(experience_controller.find_by_id(experience_id)), HTTPStatus.OK)


@experience_bp.route('/<int:experience_id>', methods=['PUT'])
def update_experience(experience_id: int) -> Response:
    content = request.get_json()
    experience = Experience.create_from_dto(content)
    experience_controller.update(experience_id, experience)
    return make_response("Experience updated", HTTPStatus.OK)


@experience_bp.route('/<int:experience_id>', methods=['PATCH'])
def patch_experience(experience_id: int) -> Response:
    content = request.get_json()
    experience_controller.patch(experience_id, content)
    return make_response("Experience updated", HTTPStatus.OK)


@experience_bp.route('/<int:experience_id>', methods=['DELETE'])
def delete_experience(experience_id: int) -> Response:
    experience_controller.delete(experience_id)
    return make_response("Experience deleted", HTTPStatus.OK)
