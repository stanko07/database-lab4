from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from app.controller   import interviews_controller
from ..domain.interviews import Interview

interviews_bp = Blueprint('interviews', __name__, url_prefix='/interviews')


@interviews_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Interviews'],
    'summary': 'Get all interviews',
    'description': 'Returns a list of all interviews',
    'responses': {
        200: {
            'description': 'Successfully retrieved interviews list'
        }
    }
})
def get_all_interview_results() -> Response:
    return make_response(jsonify(interviews_controller.find_all()), HTTPStatus.OK)


@interviews_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Interviews'],
    'summary': 'Create a new interview',
    'description': 'Creates a new interview record',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'candidate_id': {'type': 'integer', 'example': 1},
                    'vacancy_id': {'type': 'integer', 'example': 1},
                    'interview_date': {'type': 'string', 'format': 'date', 'example': '2024-01-15'},
                    'status': {'type': 'string', 'example': 'scheduled'}
                },
                'required': ['candidate_id', 'vacancy_id', 'interview_date']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Interview successfully created'
        }
    }
})
def create_interview_result() -> Response:
    content = request.get_json()
    interview = Interview.create_from_dto(content)
    interviews_controller.create(interview)
    return make_response(jsonify(interview.put_into_dto()), HTTPStatus.CREATED)


@interviews_bp.route('/<int:interviews_id>', methods=['GET'])
@swag_from({
    'tags': ['Interviews'],
    'summary': 'Get interview by ID',
    'description': 'Returns information about a specific interview',
    'parameters': [
        {
            'name': 'interviews_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Interview ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Interview found'
        },
        404: {
            'description': 'Interview not found'
        }
    }
})
def get_interview(interviews_id: int) -> Response:
    return make_response(jsonify(interviews_controller.find_by_id(interviews_id)), HTTPStatus.OK)


@interviews_bp.route('/<int:interviews_id>', methods=['PUT'])
@swag_from({
    'tags': ['Interviews'],
    'summary': 'Update interview',
    'description': 'Fully updates interview data',
    'parameters': [
        {
            'name': 'interviews_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Interview ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'candidate_id': {'type': 'integer'},
                    'vacancy_id': {'type': 'integer'},
                    'interview_date': {'type': 'string', 'format': 'date'},
                    'status': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Interview updated'
        },
        404: {
            'description': 'Interview not found'
        }
    }
})
def update_interview(interviews_id: int) -> Response:
    content = request.get_json()
    interviews = Interview.create_from_dto(content)
    interviews_controller.update(interviews_id, interviews)
    return make_response("Interview  updated", HTTPStatus.OK)


@interviews_bp.route('/<int:interviews_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Interviews'],
    'summary': 'Partially update interview',
    'description': 'Updates specific fields of an interview',
    'parameters': [
        {
            'name': 'interviews_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Interview ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'candidate_id': {'type': 'integer'},
                    'vacancy_id': {'type': 'integer'},
                    'interview_date': {'type': 'string', 'format': 'date'},
                    'status': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Interview updated'
        },
        404: {
            'description': 'Interview not found'
        }
    }
})
def patch_interview(interviews_id: int) -> Response:
    content = request.get_json()
    interviews_controller.patch(interviews_id, content)
    return make_response("Interview updated", HTTPStatus.OK)


@interviews_bp.route('/<int:interviews_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Interviews'],
    'summary': 'Delete interview',
    'description': 'Deletes an interview from the database',
    'parameters': [
        {
            'name': 'interviews_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Interview ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Interview deleted'
        },
        404: {
            'description': 'Interview not found'
        }
    }
})
def delete_interview(interviews_id: int) -> Response:
    interviews_controller.delete(interviews_id)
    return make_response("Interview  deleted", HTTPStatus.OK)
