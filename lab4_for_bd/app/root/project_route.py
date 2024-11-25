from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller   import projects_controller
from ..domain.projects import Project , insert_projects , get_through_capacity

project_bp = Blueprint('projects', __name__, url_prefix='/projects')


@project_bp.route('', methods=['GET'])
def get_all_interview_results() -> Response:
    return make_response(jsonify(projects_controller.find_all()), HTTPStatus.OK)


@project_bp.route('', methods=['POST'])
def create_interview_result() -> Response:
    content = request.get_json()
    project = Project.create_from_dto(content)
    projects_controller.create(project)
    return make_response(jsonify(project.put_into_dto()), HTTPStatus.CREATED)


@project_bp.route('/<int:project_id>', methods=['GET'])
def get_project(project_id: int) -> Response:
    return make_response(jsonify(projects_controller.find_by_id(project_id)), HTTPStatus.OK)


@project_bp.route('/<int:project_id>', methods=['PUT'])
def update_project(project_id: int) -> Response:
    content = request.get_json()
    project = Project.create_from_dto(content)
    projects_controller.update(project_id, project)
    return make_response("project updated", HTTPStatus.OK)


@project_bp.route('/<int:project_id>', methods=['PATCH'])
def patch_project(project_id: int) -> Response:
    content = request.get_json()
    projects_controller.patch(project_id, content)
    return make_response("projectlt updated", HTTPStatus.OK)


@project_bp.route('/<int:project_id>', methods=['DELETE'])
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