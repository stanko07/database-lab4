from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller   import vacanci_controller
from ..domain.vacanci import Vacanci

vacancii_bp = Blueprint('vacancii', __name__, url_prefix='/vacancii')


@vacancii_bp.route('', methods=['GET'])
def get_all_interview_results() -> Response:
    return make_response(jsonify(vacanci_controller.find_all()), HTTPStatus.OK)


@vacancii_bp.route('', methods=['POST'])
def create_interview_result() -> Response:
    content = request.get_json()
    vacancii = Vacanci.create_from_dto(content)
    vacanci_controller.create(vacancii)
    return make_response(jsonify(vacancii.put_into_dto()), HTTPStatus.CREATED)


@vacancii_bp.route('/<int:vacancii_id>', methods=['GET'])
def get_interview_result(vacancii_id: int) -> Response:
    return make_response(jsonify(vacanci_controller.find_by_id(vacancii_id)), HTTPStatus.OK)


@vacancii_bp.route('/<int:vacancii_id>', methods=['PUT'])
def update_interview_result(vacancii_id: int) -> Response:
    content = request.get_json()
    vacancii = Vacanci.create_from_dto(content)
    vacanci_controller.update(vacancii_id, vacancii)
    return make_response("Interview result updated", HTTPStatus.OK)


@vacancii_bp.route('/<int:vacancii_id>', methods=['PATCH'])
def patch_interview_result(vacancii_id: int) -> Response:
    content = request.get_json()
    vacanci_controller.patch(vacancii_id, content)
    return make_response("Interview result updated", HTTPStatus.OK)


@vacancii_bp.route('/<int:vacancii_id>', methods=['DELETE'])
def delete_interview_result(vacancii_id: int) -> Response:
    vacanci_controller.delete(vacancii_id)
    return make_response("Interview result deleted", HTTPStatus.OK)
