from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from app.controller import candidate_have_skills_controller
from ..domain.candidate_have_skills import CandidateHaveSkills

candidate_have_skills_bp = Blueprint('candidate_have_skills', __name__, url_prefix='/candidate_have_skills')


@candidate_have_skills_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Candidate Skills'],
    'summary': 'Get all candidate skills',
    'description': 'Returns a list of all candidate-skill relationships',
    'responses': {
        200: {
            'description': 'Successfully retrieved candidate skills list'
        }
    }
})
def get_all_goals() -> Response:
    return make_response(jsonify(candidate_have_skills_controller.find_all()), HTTPStatus.OK)


@candidate_have_skills_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Candidate Skills'],
    'summary': 'Create a new candidate-skill relationship',
    'description': 'Associates a skill with a candidate',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'candidate_id': {'type': 'integer', 'example': 1},
                    'skill_id': {'type': 'integer', 'example': 1},
                    'proficiency_level': {'type': 'string', 'example': 'Expert'},
                    'years_of_experience': {'type': 'integer', 'example': 5}
                },
                'required': ['candidate_id', 'skill_id']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Candidate skill successfully created'
        }
    }
})
def create_goal() -> Response:
    content = request.get_json()
    candidate_have_skills = CandidateHaveSkills.create_from_dto(content)
    candidate_have_skills_controller.create(candidate_have_skills)
    return make_response(jsonify(candidate_have_skills.put_into_dto()), HTTPStatus.CREATED)


@candidate_have_skills_bp.route('/<int:candidate_have_skills_id>', methods=['GET'])
@swag_from({
    'tags': ['Candidate Skills'],
    'summary': 'Get candidate skill by ID',
    'description': 'Returns information about a specific candidate-skill relationship',
    'parameters': [
        {
            'name': 'candidate_have_skills_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Candidate skill ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Candidate skill found'
        },
        404: {
            'description': 'Candidate skill not found'
        }
    }
})
def get_goal(candidate_have_skills_id: int) -> Response:
    return make_response(jsonify(candidate_have_skills_controller.find_by_id(candidate_have_skills_id)), HTTPStatus.OK)


@candidate_have_skills_bp.route('/<int:candidate_have_skills_id>', methods=['PUT'])
@swag_from({
    'tags': ['Candidate Skills'],
    'summary': 'Update candidate skill',
    'description': 'Fully updates candidate-skill relationship data',
    'parameters': [
        {
            'name': 'candidate_have_skills_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Candidate skill ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'candidate_id': {'type': 'integer'},
                    'skill_id': {'type': 'integer'},
                    'proficiency_level': {'type': 'string'},
                    'years_of_experience': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Candidate skill updated'
        },
        404: {
            'description': 'Candidate skill not found'
        }
    }
})
def update_goal(candidate_have_skills_id: int) -> Response:
    content = request.get_json()
    candidate_have_skills = CandidateHaveSkills.create_from_dto(content)
    candidate_have_skills_controller.update(candidate_have_skills_id, candidate_have_skills)
    return make_response("Goal updated", HTTPStatus.OK)


@candidate_have_skills_bp.route('/<int:candidate_have_skills_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Candidate Skills'],
    'summary': 'Partially update candidate skill',
    'description': 'Updates specific fields of a candidate-skill relationship',
    'parameters': [
        {
            'name': 'candidate_have_skills_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Candidate skill ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'candidate_id': {'type': 'integer'},
                    'skill_id': {'type': 'integer'},
                    'proficiency_level': {'type': 'string'},
                    'years_of_experience': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Candidate skill updated'
        },
        404: {
            'description': 'Candidate skill not found'
        }
    }
})
def patch_goal(candidate_have_skills_id: int) -> Response:
    content = request.get_json()
    candidate_have_skills_controller.patch(candidate_have_skills_id, content)
    return make_response("Goal updated", HTTPStatus.OK)


@candidate_have_skills_bp.route('/<int:candidate_have_skills_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Candidate Skills'],
    'summary': 'Delete candidate skill',
    'description': 'Deletes a candidate-skill relationship from the database',
    'parameters': [
        {
            'name': 'candidate_have_skills_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Candidate skill ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Candidate skill deleted'
        },
        404: {
            'description': 'Candidate skill not found'
        }
    }
})
def delete_goal(candidate_have_skills_id: int) -> Response:
    candidate_have_skills_controller.delete(candidate_have_skills_id)
    return make_response("Goal deleted", HTTPStatus.OK)
