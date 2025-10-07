from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from app.controller   import experience_controller
from ..domain.experience import Experience

experience_bp = Blueprint('experience', __name__, url_prefix='/experience')


@experience_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Experience'],
    'summary': 'Get all experiences',
    'description': 'Returns a list of all candidate experiences',
    'responses': {
        200: {
            'description': 'Successfully retrieved experiences list'
        }
    }
})
def get_all_experiences() -> Response:
    return make_response(jsonify(experience_controller.find_all()), HTTPStatus.OK)


@experience_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Experience'],
    'summary': 'Create a new experience',
    'description': 'Creates a new experience record for a candidate',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'candidate_id': {'type': 'integer', 'example': 1},
                    'company_name': {'type': 'string', 'example': 'Tech Corp'},
                    'position': {'type': 'string', 'example': 'Software Engineer'},
                    'start_date': {'type': 'string', 'format': 'date', 'example': '2020-01-01'},
                    'end_date': {'type': 'string', 'format': 'date', 'example': '2022-01-01'}
                },
                'required': ['candidate_id', 'company_name', 'position']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Experience successfully created'
        }
    }
})
def create_experience() -> Response:
    content = request.get_json()
    experience = Experience.create_from_dto(content)
    experience_controller.create(experience)
    return make_response(jsonify(experience.put_into_dto()), HTTPStatus.CREATED)


@experience_bp.route('/<int:experience_id>', methods=['GET'])
@swag_from({
    'tags': ['Experience'],
    'summary': 'Get experience by ID',
    'description': 'Returns information about a specific experience',
    'parameters': [
        {
            'name': 'experience_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Experience ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Experience found'
        },
        404: {
            'description': 'Experience not found'
        }
    }
})
def get_experience(experience_id: int) -> Response:
    return make_response(jsonify(experience_controller.find_by_id(experience_id)), HTTPStatus.OK)


@experience_bp.route('/<int:experience_id>', methods=['PUT'])
@swag_from({
    'tags': ['Experience'],
    'summary': 'Update experience',
    'description': 'Fully updates experience data',
    'parameters': [
        {
            'name': 'experience_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Experience ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'candidate_id': {'type': 'integer'},
                    'company_name': {'type': 'string'},
                    'position': {'type': 'string'},
                    'start_date': {'type': 'string', 'format': 'date'},
                    'end_date': {'type': 'string', 'format': 'date'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Experience updated'
        },
        404: {
            'description': 'Experience not found'
        }
    }
})
def update_experience(experience_id: int) -> Response:
    content = request.get_json()
    experience = Experience.create_from_dto(content)
    experience_controller.update(experience_id, experience)
    return make_response("Experience updated", HTTPStatus.OK)


@experience_bp.route('/<int:experience_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Experience'],
    'summary': 'Partially update experience',
    'description': 'Updates specific fields of an experience',
    'parameters': [
        {
            'name': 'experience_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Experience ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'candidate_id': {'type': 'integer'},
                    'company_name': {'type': 'string'},
                    'position': {'type': 'string'},
                    'start_date': {'type': 'string', 'format': 'date'},
                    'end_date': {'type': 'string', 'format': 'date'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Experience updated'
        },
        404: {
            'description': 'Experience not found'
        }
    }
})
def patch_experience(experience_id: int) -> Response:
    content = request.get_json()
    experience_controller.patch(experience_id, content)
    return make_response("Experience updated", HTTPStatus.OK)


@experience_bp.route('/<int:experience_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Experience'],
    'summary': 'Delete experience',
    'description': 'Deletes an experience from the database',
    'parameters': [
        {
            'name': 'experience_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Experience ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Experience deleted'
        },
        404: {
            'description': 'Experience not found'
        }
    }
})
def delete_experience(experience_id: int) -> Response:
    experience_controller.delete(experience_id)
    return make_response("Experience deleted", HTTPStatus.OK)
