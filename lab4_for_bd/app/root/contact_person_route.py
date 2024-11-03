from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from app.controller   import contact_person_controller
from ..domain.contact_person import ContactPerson

contact_person_bp = Blueprint('contact_person', __name__, url_prefix='/contact_person')


@contact_person_bp.route('', methods=['GET'])
def get_all_companies() -> Response:
    return make_response(jsonify(contact_person_controller.find_all()), HTTPStatus.OK)


@contact_person_bp.route('', methods=['POST'])
def create_company() -> Response:
    content = request.get_json()
    contact_person = ContactPerson.create_from_dto(content)
    contact_person_controller.create(contact_person)
    return make_response(jsonify(contact_person.put_into_dto()), HTTPStatus.CREATED)


@contact_person_bp.route('/<int:contact_person_id>', methods=['GET'])
def get_company(contact_person_id: int) -> Response:
    return make_response(jsonify(contact_person_controller.find_by_id(contact_person_id)), HTTPStatus.OK)


@contact_person_bp.route('/<int:contact_person_id>', methods=['PUT'])
def update_company(contact_person_id: int) -> Response:
    content = request.get_json()
    contact_person = ContactPerson.create_from_dto(content)
    contact_person_controller.update(contact_person_id, contact_person)
    return make_response("Company updated", HTTPStatus.OK)


@contact_person_bp.route('/<int:contact_person_id>', methods=['PATCH'])
def patch_company(contact_person_id: int) -> Response:
    content = request.get_json()
    contact_person_controller.patch(contact_person_id, content)
    return make_response("Company updated", HTTPStatus.OK)


@contact_person_bp.route('/<int:contact_person_id>', methods=['DELETE'])
def delete_company(contact_person_id: int) -> Response:
    contact_person_controller.delete(contact_person_id)
    return make_response("Company deleted", HTTPStatus.OK)
