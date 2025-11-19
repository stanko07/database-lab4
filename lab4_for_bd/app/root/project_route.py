from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from app.controller   import projects_controller
from ..domain.projects import Project , insert_projects , get_through_capacity

project_bp = Blueprint('projects', __name__, url_prefix='/projects')


@project_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Projects'],
    'summary': 'Get all projects',
    'description': 'Returns a list of all projects',
    'responses': {
        200: {
            'description': 'Successfully retrieved projects list'
        }
    }
})
def get_all_interview_results() -> Response:
    return make_response(jsonify(projects_controller.find_all()), HTTPStatus.OK)


@project_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Projects'],
    'summary': 'Create a new project',
    'description': 'Creates a new project record',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'E-commerce Platform'},
                    'description': {'type': 'string', 'example': 'Online shopping platform'},
                    'company_id': {'type': 'integer', 'example': 1},
                    'start_date': {'type': 'string', 'format': 'date', 'example': '2024-01-01'}
                },
                'required': ['name']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Project successfully created'
        }
    }
})
def create_interview_result() -> Response:
    content = request.get_json()
    project = Project.create_from_dto(content)
    projects_controller.create(project)
    return make_response(jsonify(project.put_into_dto()), HTTPStatus.CREATED)


@project_bp.route('/<int:project_id>', methods=['GET'])
@swag_from({
    'tags': ['Projects'],
    'summary': 'Get project by ID',
    'description': 'Returns information about a specific project',
    'parameters': [
        {
            'name': 'project_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Project ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Project found'
        },
        404: {
            'description': 'Project not found'
        }
    }
})
def get_project(project_id: int) -> Response:
    return make_response(jsonify(projects_controller.find_by_id(project_id)), HTTPStatus.OK)


@project_bp.route('/<int:project_id>', methods=['PUT'])
@swag_from({
    'tags': ['Projects'],
    'summary': 'Update project',
    'description': 'Fully updates project data',
    'parameters': [
        {
            'name': 'project_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Project ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'description': {'type': 'string'},
                    'company_id': {'type': 'integer'},
                    'start_date': {'type': 'string', 'format': 'date'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Project updated'
        },
        404: {
            'description': 'Project not found'
        }
    }
})
def update_project(project_id: int) -> Response:
    content = request.get_json()
    project = Project.create_from_dto(content)
    projects_controller.update(project_id, project)
    return make_response("project updated", HTTPStatus.OK)


@project_bp.route('/<int:project_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Projects'],
    'summary': 'Partially update project',
    'description': 'Updates specific fields of a project',
    'parameters': [
        {
            'name': 'project_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Project ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'description': {'type': 'string'},
                    'company_id': {'type': 'integer'},
                    'start_date': {'type': 'string', 'format': 'date'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Project updated'
        },
        404: {
            'description': 'Project not found'
        }
    }
})
def patch_project(project_id: int) -> Response:
    content = request.get_json()
    projects_controller.patch(project_id, content)
    return make_response("projectlt updated", HTTPStatus.OK)


@project_bp.route('/<int:project_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Projects'],
    'summary': 'Delete project',
    'description': 'Deletes a project from the database',
    'parameters': [
        {
            'name': 'project_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Project ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Project deleted'
        },
        404: {
            'description': 'Project not found'
        }
    }
})
def delete_project(project_id: int) -> Response:
    projects_controller.delete(project_id)
    return make_response("projectdeleted", HTTPStatus.OK)



@project_bp.route('/auto_insert', methods=['POST'])
def auto_projects_create() -> Response | tuple[Response, int]:
    num_projects = request.args.get('amount')
    result = insert_projects(int(num_projects))
    if result != -1:
        res = [player.put_into_dto() for player in result]
        return jsonify({"new_projects": res})
    else:
        return jsonify({"error"}), 400


@project_bp.route('capacity', methods=['GET'])
def get_capacity() -> Response | tuple[Response, int]:
    stat_type = request.args.get('stat_type').upper()
    result = get_through_capacity(stat_type)
    if result != -1:
        return jsonify({stat_type: result})
    else:
        return jsonify({"error": "Invalid stat_type. Use MAX, MIN, SUM, or AVG"}), 400