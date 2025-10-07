from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from app.controller import candidates_controller
from app.domain.candidates import Candidates

candidates_controller_bp = Blueprint('candidates', __name__, url_prefix='/candidates')


@candidates_controller_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Candidates'],
    'summary': 'Get all candidates',
    'description': 'Returns a list of all candidates',
    'responses': {
        200: {
            'description': 'Successfully retrieved candidates list',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'surname': {'type': 'string'},
                        'email': {'type': 'string'},
                        'phone': {'type': 'string'}
                    }
                }
            }
        }
    }
})
def get_all_companies() -> Response:
    return make_response(jsonify(candidates_controller.find_all()), HTTPStatus.OK)


@candidates_controller_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Candidates'],
    'summary': 'Create a new candidate',
    'description': 'Creates a new candidate with the provided data',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'John'},
                    'surname': {'type': 'string', 'example': 'Doe'},
                    'email': {'type': 'string', 'example': 'john.doe@example.com'},
                    'phone': {'type': 'string', 'example': '380991234567'}
                },
                'required': ['name', 'surname', 'email', 'phone']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Candidate successfully created'
        }
    }
})
def create_company() -> Response:
    content = request.get_json()
    company = Candidates.create_from_dto(content)
    candidates_controller.create(company)
    return make_response(jsonify(company.put_into_dto()), HTTPStatus.CREATED)


@candidates_controller_bp.route('/<int:candidates_id>', methods=['GET'])
@swag_from({
    'tags': ['Candidates'],
    'summary': 'Get candidate by ID',
    'description': 'Returns information about a specific candidate',
    'parameters': [
        {
            'name': 'candidates_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Candidate ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Candidate found'
        },
        404: {
            'description': 'Candidate not found'
        }
    }
})
def get_company(candidates_id: int) -> Response:
    return make_response(jsonify(candidates_controller.find_by_id(candidates_id)), HTTPStatus.OK)


@candidates_controller_bp.route('/<int:candidates_id>', methods=['PUT'])
@swag_from({
    'tags': ['Candidates'],
    'summary': 'Update candidate',
    'description': 'Fully updates candidate data',
    'parameters': [
        {
            'name': 'candidates_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Candidate ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'surname': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Candidate updated'
        },
        404: {
            'description': 'Candidate not found'
        }
    }
})
def update_company(candidates_id: int) -> Response:
    content = request.get_json()
    company = Candidates.create_from_dto(content)
    candidates_controller.update(candidates_id, company)
    return make_response("Candidate create", HTTPStatus.OK)


@candidates_controller_bp.route('/<int:candidates_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Candidates'],
    'summary': 'Partially update candidate',
    'description': 'Updates specific fields of a candidate',
    'parameters': [
        {
            'name': 'candidates_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Candidate ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'surname': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Candidate updated'
        },
        404: {
            'description': 'Candidate not found'
        }
    }
})
def patch_company(candidates_id: int) -> Response:
    content = request.get_json()
    candidates_controller.patch(candidates_id, content)
    return make_response("Candidate updated", HTTPStatus.OK)


@candidates_controller_bp.route('/<int:candidates_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Candidates'],
    'summary': 'Delete candidate',
    'description': 'Deletes a candidate from the database',
    'parameters': [
        {
            'name': 'candidates_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Candidate ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Candidate deleted'
        },
        404: {
            'description': 'Candidate not found'
        }
    }
})
def delete_company(candidates_id: int) -> Response:
    candidates_controller.delete(candidates_id)
    return make_response("Candidate deleted", HTTPStatus.OK)
