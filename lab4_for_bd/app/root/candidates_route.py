from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller import candidates_controller
from app.domain.candidates import Candidates

candidates_controller_bp = Blueprint('candidates', __name__, url_prefix='/candidates')


@candidates_controller_bp.route('', methods=['GET'])
def get_all_companies() -> Response:
    return make_response(jsonify(candidates_controller.find_all()), HTTPStatus.OK)


@candidates_controller_bp.route('', methods=['POST'])
def create_company() -> Response:
    content = request.get_json()
    company = Candidates.create_from_dto(content)
    candidates_controller.create(company)
    return make_response(jsonify(company.put_into_dto()), HTTPStatus.CREATED)


@candidates_controller_bp.route('/<int:candidates_id>', methods=['GET'])
def get_company(candidates_id: int) -> Response:
    return make_response(jsonify(candidates_controller.find_by_id(candidates_id)), HTTPStatus.OK)


@candidates_controller_bp.route('/<int:candidates_id>', methods=['PUT'])
def update_company(candidates_id: int) -> Response:
    content = request.get_json()
    company = Candidates.create_from_dto(content)
    candidates_controller.update(candidates_id, company)
    return make_response("Candidate create", HTTPStatus.OK)


@candidates_controller_bp.route('/<int:candidates_id>', methods=['PATCH'])
def patch_company(candidates_id: int) -> Response:
    content = request.get_json()
    candidates_controller.patch(candidates_id, content)
    return make_response("Candidate updated", HTTPStatus.OK)


@candidates_controller_bp.route('/<int:candidates_id>', methods=['DELETE'])
def delete_company(candidates_id: int) -> Response:
    candidates_controller.delete(candidates_id)
    return make_response("Candidate deleted", HTTPStatus.OK)
