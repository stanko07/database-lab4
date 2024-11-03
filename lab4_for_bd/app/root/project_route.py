from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller   import projects_controller
from ..domain.projects import Project

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
