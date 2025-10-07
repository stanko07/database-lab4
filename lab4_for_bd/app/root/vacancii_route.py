from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from app.controller   import vacanci_controller
from ..domain.vacanci import Vacanci

vacancii_bp = Blueprint('vacancii', __name__, url_prefix='/vacancii')


@vacancii_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Vacancies'],
    'summary': 'Get all vacancies',
    'description': 'Returns a list of all vacancies',
    'responses': {
        200: {
            'description': 'Successfully retrieved vacancies list'
        }
    }
})
def get_all_interview_results() -> Response:
    return make_response(jsonify(vacanci_controller.find_all()), HTTPStatus.OK)


@vacancii_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Vacancies'],
    'summary': 'Create a new vacancy',
    'description': 'Creates a new vacancy record',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string', 'example': 'Senior Python Developer'},
                    'description': {'type': 'string', 'example': 'Looking for experienced Python developer'},
                    'company_id': {'type': 'integer', 'example': 1},
                    'salary': {'type': 'number', 'example': 5000},
                    'status': {'type': 'string', 'example': 'open'}
                },
                'required': ['title', 'company_id']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Vacancy successfully created'
        }
    }
})
def create_interview_result() -> Response:
    content = request.get_json()
    vacancii = Vacanci.create_from_dto(content)
    vacanci_controller.create(vacancii)
    return make_response(jsonify(vacancii.put_into_dto()), HTTPStatus.CREATED)


@vacancii_bp.route('/<int:vacancii_id>', methods=['GET'])
@swag_from({
    'tags': ['Vacancies'],
    'summary': 'Get vacancy by ID',
    'description': 'Returns information about a specific vacancy',
    'parameters': [
        {
            'name': 'vacancii_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Vacancy ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Vacancy found'
        },
        404: {
            'description': 'Vacancy not found'
        }
    }
})
def get_interview_result(vacancii_id: int) -> Response:
    return make_response(jsonify(vacanci_controller.find_by_id(vacancii_id)), HTTPStatus.OK)


@vacancii_bp.route('/<int:vacancii_id>', methods=['PUT'])
@swag_from({
    'tags': ['Vacancies'],
    'summary': 'Update vacancy',
    'description': 'Fully updates vacancy data',
    'parameters': [
        {
            'name': 'vacancii_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Vacancy ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'company_id': {'type': 'integer'},
                    'salary': {'type': 'number'},
                    'status': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Vacancy updated'
        },
        404: {
            'description': 'Vacancy not found'
        }
    }
})
def update_interview_result(vacancii_id: int) -> Response:
    content = request.get_json()
    vacancii = Vacanci.create_from_dto(content)
    vacanci_controller.update(vacancii_id, vacancii)
    return make_response("Interview result updated", HTTPStatus.OK)


@vacancii_bp.route('/<int:vacancii_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Vacancies'],
    'summary': 'Partially update vacancy',
    'description': 'Updates specific fields of a vacancy',
    'parameters': [
        {
            'name': 'vacancii_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Vacancy ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'company_id': {'type': 'integer'},
                    'salary': {'type': 'number'},
                    'status': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Vacancy updated'
        },
        404: {
            'description': 'Vacancy not found'
        }
    }
})
def patch_interview_result(vacancii_id: int) -> Response:
    content = request.get_json()
    vacanci_controller.patch(vacancii_id, content)
    return make_response("Interview result updated", HTTPStatus.OK)


@vacancii_bp.route('/<int:vacancii_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Vacancies'],
    'summary': 'Delete vacancy',
    'description': 'Deletes a vacancy from the database',
    'parameters': [
        {
            'name': 'vacancii_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Vacancy ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Vacancy deleted'
        },
        404: {
            'description': 'Vacancy not found'
        }
    }
})
def delete_interview_result(vacancii_id: int) -> Response:
    vacanci_controller.delete(vacancii_id)
    return make_response("Interview result deleted", HTTPStatus.OK)
