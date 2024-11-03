from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller   import interviews_controller
from ..domain.interviews import Interview

interviews_bp = Blueprint('interviews', __name__, url_prefix='/interviews')


@interviews_bp.route('', methods=['GET'])
def get_all_interview_results() -> Response:
    return make_response(jsonify(interviews_controller.find_all()), HTTPStatus.OK)


@interviews_bp.route('', methods=['POST'])
def create_interview_result() -> Response:
    content = request.get_json()
    interview = Interview.create_from_dto(content)
    interviews_controller.create(interview)
    return make_response(jsonify(interview.put_into_dto()), HTTPStatus.CREATED)


@interviews_bp.route('/<int:interviews_id>', methods=['GET'])
def get_interview(interviews_id: int) -> Response:
    return make_response(jsonify(interviews_controller.find_by_id(interviews_id)), HTTPStatus.OK)


@interviews_bp.route('/<int:interviews_id>', methods=['PUT'])
def update_interview(interviews_id: int) -> Response:
    content = request.get_json()
    interviews = Interview.create_from_dto(content)
    interviews_controller.update(interviews_id, interviews)
    return make_response("Interview  updated", HTTPStatus.OK)


@interviews_bp.route('/<int:interviews_id>', methods=['PATCH'])
def patch_interview(interviews_id: int) -> Response:
    content = request.get_json()
    interviews_controller.patch(interviews_id, content)
    return make_response("Interview updated", HTTPStatus.OK)


@interviews_bp.route('/<int:interviews_id>', methods=['DELETE'])
def delete_interview(interviews_id: int) -> Response:
    interviews_controller.delete(interviews_id)
    return make_response("Interview  deleted", HTTPStatus.OK)
