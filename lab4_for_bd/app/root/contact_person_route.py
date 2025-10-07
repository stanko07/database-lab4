from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flasgger import swag_from
from app.controller   import contact_person_controller
from ..domain.contact_person import ContactPerson

contact_person_bp = Blueprint('contact_person', __name__, url_prefix='/contact_person')


@contact_person_bp.route('', methods=['GET'])
@swag_from({
    'tags': ['Contact Persons'],
    'summary': 'Get all contact persons',
    'description': 'Returns a list of all contact persons',
    'responses': {
        200: {
            'description': 'Successfully retrieved contact persons list'
        }
    }
})
def get_all_companies() -> Response:
    return make_response(jsonify(contact_person_controller.find_all()), HTTPStatus.OK)


@contact_person_bp.route('', methods=['POST'])
@swag_from({
    'tags': ['Contact Persons'],
    'summary': 'Create a new contact person',
    'description': 'Creates a new contact person with the provided data',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string', 'example': 'Jane'},
                    'surname': {'type': 'string', 'example': 'Smith'},
                    'email': {'type': 'string', 'example': 'jane.smith@company.com'},
                    'phone': {'type': 'string', 'example': '380991234567'},
                    'company_id': {'type': 'integer', 'example': 1}
                },
                'required': ['name', 'surname', 'email', 'phone']
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Contact person successfully created'
        }
    }
})
def create_company() -> Response:
    content = request.get_json()
    contact_person = ContactPerson.create_from_dto(content)
    contact_person_controller.create(contact_person)
    return make_response(jsonify(contact_person.put_into_dto()), HTTPStatus.CREATED)


@contact_person_bp.route('/<int:contact_person_id>', methods=['GET'])
@swag_from({
    'tags': ['Contact Persons'],
    'summary': 'Get contact person by ID',
    'description': 'Returns information about a specific contact person',
    'parameters': [
        {
            'name': 'contact_person_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Contact person ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Contact person found'
        },
        404: {
            'description': 'Contact person not found'
        }
    }
})
def get_company(contact_person_id: int) -> Response:
    return make_response(jsonify(contact_person_controller.find_by_id(contact_person_id)), HTTPStatus.OK)


@contact_person_bp.route('/<int:contact_person_id>', methods=['PUT'])
@swag_from({
    'tags': ['Contact Persons'],
    'summary': 'Update contact person',
    'description': 'Fully updates contact person data',
    'parameters': [
        {
            'name': 'contact_person_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Contact person ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'surname': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone': {'type': 'string'},
                    'company_id': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Contact person updated'
        },
        404: {
            'description': 'Contact person not found'
        }
    }
})
def update_company(contact_person_id: int) -> Response:
    content = request.get_json()
    contact_person = ContactPerson.create_from_dto(content)
    contact_person_controller.update(contact_person_id, contact_person)
    return make_response("Company updated", HTTPStatus.OK)


@contact_person_bp.route('/<int:contact_person_id>', methods=['PATCH'])
@swag_from({
    'tags': ['Contact Persons'],
    'summary': 'Partially update contact person',
    'description': 'Updates specific fields of a contact person',
    'parameters': [
        {
            'name': 'contact_person_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Contact person ID'
        },
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'surname': {'type': 'string'},
                    'email': {'type': 'string'},
                    'phone': {'type': 'string'},
                    'company_id': {'type': 'integer'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Contact person updated'
        },
        404: {
            'description': 'Contact person not found'
        }
    }
})
def patch_company(contact_person_id: int) -> Response:
    content = request.get_json()
    contact_person_controller.patch(contact_person_id, content)
    return make_response("Company updated", HTTPStatus.OK)


@contact_person_bp.route('/<int:contact_person_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Contact Persons'],
    'summary': 'Delete contact person',
    'description': 'Deletes a contact person from the database',
    'parameters': [
        {
            'name': 'contact_person_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Contact person ID'
        }
    ],
    'responses': {
        200: {
            'description': 'Contact person deleted'
        },
        404: {
            'description': 'Contact person not found'
        }
    }
})
def delete_company(contact_person_id: int) -> Response:
    contact_person_controller.delete(contact_person_id)
    return make_response("Company deleted", HTTPStatus.OK)
