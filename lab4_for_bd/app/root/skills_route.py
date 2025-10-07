from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from app.controller   import skills_controller
from ..domain.skills import Skill

skills_bp = Blueprint('skills', __name__, url_prefix='/skills')


@skills_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Skills'],
    'summary': 'Get all skills',
    'description': 'Returns a list of all skills',
    'responses': {
        200: {
            'description': 'Successfully retrieved skills list'
        }
    }
})
def get_all_interview_results() -> Response:
    return make_response(jsonify(skills_controller.find_all()), HTTPStatus.OK)


@skills_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Skills'],
    'summary': 'Create a new skill',
    'description': 'Creates a new skill record',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'Python'},
                    'category': {'type': 'string', 'example': 'Programming Language'},
                    'level': {'type': 'string', 'example': 'Advanced'}
                },
                'required': ['name']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Skill successfully created'
        }
    }
})
def create_interview_result() -> Response:
    content = request.get_json()
    skills = Skill.create_from_dto(content)
    skills_controller.create(skills)
    return make_response(jsonify(skills.put_into_dto()), HTTPStatus.CREATED)


@skills_bp.route('/<int:skills_id>', methods=['GET'])
@swag_from({
    'tags': ['Skills'],
    'summary': 'Get skill by ID',
    'description': 'Returns information about a specific skill',
    'parameters': [
        {
            'name': 'skills_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Skill ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Skill found'
        },
        404: {
            'description': 'Skill not found'
        }
    }
})
def get_interview_result(skills_id: int) -> Response:
    return make_response(jsonify(skills_controller.find_by_id(skills_id)), HTTPStatus.OK)


@skills_bp.route('/<int:skills_id>', methods=['PUT'])
@swag_from({
    'tags': ['Skills'],
    'summary': 'Update skill',
    'description': 'Fully updates skill data',
    'parameters': [
        {
            'name': 'skills_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Skill ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'category': {'type': 'string'},
                    'level': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Skill updated'
        },
        404: {
            'description': 'Skill not found'
        }
    }
})
def update_interview_result(skills_id: int) -> Response:
    content = request.get_json()
    skills = Skill.create_from_dto(content)
    skills_controller.update(skills_id, skills)
    return make_response("Interview result updated", HTTPStatus.OK)


@skills_bp.route('/<int:skills_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Skills'],
    'summary': 'Partially update skill',
    'description': 'Updates specific fields of a skill',
    'parameters': [
        {
            'name': 'skills_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Skill ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'category': {'type': 'string'},
                    'level': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Skill updated'
        },
        404: {
            'description': 'Skill not found'
        }
    }
})
def patch_interview_result(skills_id: int) -> Response:
    content = request.get_json()
    skills_controller.patch(skills_id, content)
    return make_response("Interview result updated", HTTPStatus.OK)


@skills_bp.route('/<int:skills_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Skills'],
    'summary': 'Delete skill',
    'description': 'Deletes a skill from the database',
    'parameters': [
        {
            'name': 'skills_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Skill ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Skill deleted'
        },
        404: {
            'description': 'Skill not found'
        }
    }
})
def delete_interview_result(skills_id: int) -> Response:
    skills_controller.delete(skills_id)
    return make_response("Interview result deleted", HTTPStatus.OK)
