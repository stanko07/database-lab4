from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from  app.controller  import company_controller
from ..domain.company import Company, insert_company

company_bp = Blueprint('company', __name__, url_prefix='/company')


@company_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Companies'],
    'summary': 'Get all companies',
    'description': 'Returns a list of all companies',
    'responses': {
        200: {
            'description': 'Successfully retrieved companies list'
        }
    }
})
def get_all_companies() -> Response:
    return make_response(jsonify(company_controller.find_all()), HTTPStatus.OK)


@company_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Companies'],
    'summary': 'Create a new company',
    'description': 'Creates a new company with the provided data',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'TechCorp'},
                    'address': {'type': 'string', 'example': '123 Main St'}
                },
                'required': ['name']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Company successfully created'
        }
    }
})
def create_company() -> Response:
    content = request.get_json()
    company = Company.create_from_dto(content)
    company_controller.create(company)
    return make_response(jsonify(company.put_into_dto()), HTTPStatus.CREATED)


@company_bp.route('/<int:company_id>', methods=['GET'])
@swag_from({
    'tags': ['Companies'],
    'summary': 'Get company by ID',
    'description': 'Returns information about a specific company',
    'parameters': [
        {
            'name': 'company_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Company ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Company found'
        },
        404: {
            'description': 'Company not found'
        }
    }
})
def get_company(company_id: int) -> Response:
    return make_response(jsonify(company_controller.find_by_id(company_id)), HTTPStatus.OK)


@company_bp.route('/<int:company_id>', methods=['PUT'])
@swag_from({
    'tags': ['Companies'],
    'summary': 'Update company',
    'description': 'Fully updates company data',
    'parameters': [
        {
            'name': 'company_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Company ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'address': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Company updated'
        },
        404: {
            'description': 'Company not found'
        }
    }
})
def update_company(company_id: int) -> Response:
    content = request.get_json()
    company = Company.create_from_dto(content)
    company_controller.update(company_id, company)
    return make_response("Company create", HTTPStatus.OK)


@company_bp.route('/<int:company_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Companies'],
    'summary': 'Partially update company',
    'description': 'Updates specific fields of a company',
    'parameters': [
        {
            'name': 'company_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Company ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'address': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Company updated'
        },
        404: {
            'description': 'Company not found'
        }
    }
})
def patch_company(company_id: int) -> Response:
    content = request.get_json()
    company_controller.patch(company_id, content)
    return make_response("Company updated", HTTPStatus.OK)


@company_bp.route('/<int:company_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Companies'],
    'summary': 'Delete company',
    'description': 'Deletes a company from the database',
    'parameters': [
        {
            'name': 'company_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Company ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Company deleted'
        },
        404: {
            'description': 'Company not found'
        }
    }
})
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

