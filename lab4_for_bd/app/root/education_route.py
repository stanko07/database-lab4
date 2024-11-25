from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller import education_controller
from ..domain.education import Education

education_controller_bp = Blueprint('education', __name__, url_prefix='/education')


@education_controller_bp.route('', methods=['GET'])
def get_all_education() -> Response:
    return make_response(jsonify(education_controller.find_all()), HTTPStatus.OK)


@education_controller_bp.route('', methods=['POST'])
def create_education() -> Response:
    content = request.get_json()
    education = Education.create_from_dto(content)
    education_controller.create(education)
    return make_response(jsonify(education.put_into_dto()), HTTPStatus.CREATED)


@education_controller_bp.route('/<int:education_id>', methods=['GET'])
def get_education(education_id: int) -> Response:
    return make_response(jsonify(education_controller.find_by_id(education_id)), HTTPStatus.OK)


@education_controller_bp.route('/<int:education_id>', methods=['PUT'])
def update_education(education_id: int) -> Response:
    content = request.get_json()
    education = Education.create_from_dto(content)
    education_controller.update(education_id, education)
    return make_response("education create", HTTPStatus.OK)


@education_controller_bp.route('/<int:education_id>', methods=['PATCH'])
def patch_education(education_id: int) -> Response:
    content = request.get_json()
    education_controller.patch(education_id, content)
    return make_response("education updated", HTTPStatus.OK)


@education_controller_bp.route('/<int:education_id>', methods=['DELETE'])
def delete_education(education_id: int) -> Response:
    education_controller.delete(education_id)
    return make_response("education deleted", HTTPStatus.OK)
