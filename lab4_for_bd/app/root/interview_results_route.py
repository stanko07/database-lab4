from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller  import interview_results__controller
from ..domain.interview_results import InterviewResult

interview_results_bp = Blueprint('interview_results', __name__, url_prefix='/interview_results')


@interview_results_bp.route('', methods=['GET'])
def get_all_interview_results() -> Response:
    return make_response(jsonify(interview_results__controller.find_all()), HTTPStatus.OK)


@interview_results_bp.route('', methods=['POST'])
def create_interview_result() -> Response:
    content = request.get_json()
    interview_result = InterviewResult.create_from_dto(content)
    interview_results__controller.create(interview_result)
    return make_response(jsonify(interview_result.put_into_dto()), HTTPStatus.CREATED)


@interview_results_bp.route('/<int:interview_result_id>', methods=['GET'])
def get_interview_result(interview_result_id: int) -> Response:
    return make_response(jsonify(interview_results__controller.find_by_id(interview_result_id)), HTTPStatus.OK)


@interview_results_bp.route('/<int:interview_result_id>', methods=['PUT'])
def update_interview_result(interview_result_id: int) -> Response:
    content = request.get_json()
    interview_result = InterviewResult.create_from_dto(content)
    interview_results__controller.update(interview_result_id, interview_result)
    return make_response("Interview result updated", HTTPStatus.OK)


@interview_results_bp.route('/<int:interview_result_id>', methods=['PATCH'])
def patch_interview_result(interview_result_id: int) -> Response:
    content = request.get_json()
    interview_results__controller.patch(interview_result_id, content)
    return make_response("Interview result updated", HTTPStatus.OK)


@interview_results_bp.route('/<int:interview_result_id>', methods=['DELETE'])
def delete_interview_result(interview_result_id: int) -> Response:
    interview_results__controller.delete(interview_result_id)
    return make_response("Interview result deleted", HTTPStatus.OK)
