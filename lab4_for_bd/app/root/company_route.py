from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from  app.controller  import company_controller
from ..domain.company import Company, insert_company

company_bp = Blueprint('company', __name__, url_prefix='/company')


@company_bp.route('', methods=['GET'])
def get_all_companies() -> Response:
    return make_response(jsonify(company_controller.find_all()), HTTPStatus.OK)


@company_bp.route('', methods=['POST'])
def create_company() -> Response:
    content = request.get_json()
    company = Company.create_from_dto(content)
    company_controller.create(company)
    return make_response(jsonify(company.put_into_dto()), HTTPStatus.CREATED)


@company_bp.route('/<int:company_id>', methods=['GET'])
def get_company(company_id: int) -> Response:
    return make_response(jsonify(company_controller.find_by_id(company_id)), HTTPStatus.OK)


@company_bp.route('/<int:company_id>', methods=['PUT'])
def update_company(company_id: int) -> Response:
    content = request.get_json()
    company = Company.create_from_dto(content)
    company_controller.update(company_id, company)
    return make_response("Company create", HTTPStatus.OK)


@company_bp.route('/<int:company_id>', methods=['PATCH'])
def patch_company(company_id: int) -> Response:
    content = request.get_json()
    company_controller.patch(company_id, content)
    return make_response("Company updated", HTTPStatus.OK)


@company_bp.route('/<int:company_id>', methods=['DELETE'])
def delete_company(company_id: int) -> Response:
    company_controller.delete(company_id)
    return make_response("Company deleted", HTTPStatus.OK)


@company_bp.route('/parametrized', methods=['POST'])
def insert_parametrized() -> Response:
    content = request.get_json()
    new_company = insert_company(
        name=content['name'],
        address=content['address'],


    )
    return make_response(jsonify(new_company.put_into_dto()), HTTPStatus.CREATED)

