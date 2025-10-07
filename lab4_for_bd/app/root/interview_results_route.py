from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from app.controller  import interview_results__controller
from ..domain.interview_results import InterviewResult

interview_results_bp = Blueprint('interview_results', __name__, url_prefix='/interview_results')


@interview_results_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Interview Results'],
    'summary': 'Get all interview results',
    'description': 'Returns a list of all interview results',
    'responses': {
        200: {
            'description': 'Successfully retrieved interview results list'
        }
    }
})
def get_all_interview_results() -> Response:
    return make_response(jsonify(interview_results__controller.find_all()), HTTPStatus.OK)


@interview_results_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Interview Results'],
    'summary': 'Create a new interview result',
    'description': 'Creates a new interview result record',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'interview_id': {'type': 'integer', 'example': 1},
                    'result': {'type': 'string', 'example': 'passed'},
                    'feedback': {'type': 'string', 'example': 'Good technical skills'},
                    'score': {'type': 'number', 'example': 85}
                },
                'required': ['interview_id', 'result']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Interview result successfully created'
        }
    }
})
def create_interview_result() -> Response:
    content = request.get_json()
    interview_result = InterviewResult.create_from_dto(content)
    interview_results__controller.create(interview_result)
    return make_response(jsonify(interview_result.put_into_dto()), HTTPStatus.CREATED)


@interview_results_bp.route('/<int:interview_result_id>', methods=['GET'])
@swag_from({
    'tags': ['Interview Results'],
    'summary': 'Get interview result by ID',
    'description': 'Returns information about a specific interview result',
    'parameters': [
        {
            'name': 'interview_result_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Interview result ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Interview result found'
        },
        404: {
            'description': 'Interview result not found'
        }
    }
})
def get_interview_result(interview_result_id: int) -> Response:
    return make_response(jsonify(interview_results__controller.find_by_id(interview_result_id)), HTTPStatus.OK)


@interview_results_bp.route('/<int:interview_result_id>', methods=['PUT'])
@swag_from({
    'tags': ['Interview Results'],
    'summary': 'Update interview result',
    'description': 'Fully updates interview result data',
    'parameters': [
        {
            'name': 'interview_result_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Interview result ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'interview_id': {'type': 'integer'},
                    'result': {'type': 'string'},
                    'feedback': {'type': 'string'},
                    'score': {'type': 'number'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Interview result updated'
        },
        404: {
            'description': 'Interview result not found'
        }
    }
})
def update_interview_result(interview_result_id: int) -> Response:
    content = request.get_json()
    interview_result = InterviewResult.create_from_dto(content)
    interview_results__controller.update(interview_result_id, interview_result)
    return make_response("Interview result updated", HTTPStatus.OK)


@interview_results_bp.route('/<int:interview_result_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Interview Results'],
    'summary': 'Partially update interview result',
    'description': 'Updates specific fields of an interview result',
    'parameters': [
        {
            'name': 'interview_result_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Interview result ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'interview_id': {'type': 'integer'},
                    'result': {'type': 'string'},
                    'feedback': {'type': 'string'},
                    'score': {'type': 'number'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Interview result updated'
        },
        404: {
            'description': 'Interview result not found'
        }
    }
})
def patch_interview_result(interview_result_id: int) -> Response:
    content = request.get_json()
    interview_results__controller.patch(interview_result_id, content)
    return make_response("Interview result updated", HTTPStatus.OK)


@interview_results_bp.route('/<int:interview_result_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Interview Results'],
    'summary': 'Delete interview result',
    'description': 'Deletes an interview result from the database',
    'parameters': [
        {
            'name': 'interview_result_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Interview result ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Interview result deleted'
        },
        404: {
            'description': 'Interview result not found'
        }
    }
})
def delete_interview_result(interview_result_id: int) -> Response:
    interview_results__controller.delete(interview_result_id)
    return make_response("Interview result deleted", HTTPStatus.OK)
