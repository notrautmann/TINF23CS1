"""
Implements the CRUD-operations for the customers-table.

Functions:

    get_customers(customers_id)
    create_customers()
    update_customers(customers_id)
    delete_customers(customers_id)

Misc variables:

    customers_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.records.customers import Customers

non_id_columns = ['type',
	'company_name',
	'first_name',
	'last_name',
	'email',
	'phone',
	'address_line',
	'postal_code',
	'city',
	'country',
	'created_at',
	'updated_at']

customers_bp = Blueprint('customers',
    __name__,
    url_prefix='/customers')

@customers_bp.route('/<int:customers_id>', methods=['GET'])
@jwt_required()
def get_customers(customers_id):
    """
    Logic to get customers data
    
    Parameter:
    customers_id (int): Id of the customers-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Customers.read(customers_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@customers_bp.route('/', methods=['POST'])
@jwt_required()
def create_customers():
    """
    Logic to create customers data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Customers.create(type=request.values.get('type'),
		company_name=request.values.get('company_name'),
		first_name=request.values.get('first_name'),
		last_name=request.values.get('last_name'),
		email=request.values.get('email'),
		phone=request.values.get('phone'),
		address_line=request.values.get('address_line'),
		postal_code=request.values.get('postal_code'),
		city=request.values.get('city'),
		country=request.values.get('country'),
		created_at=request.values.get('created_at'),
		updated_at=request.values.get('updated_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@customers_bp.route('/<int:customers_id>', methods=['PUT'])
@jwt_required()
def update_customers(customers_id):
    """
    Logic to update customers data
    
    Parameter:
        customers_id (int): Id of the customers-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Customers.update(customers_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@customers_bp.route('/<int:customers_id>', methods=['DELETE'])
@jwt_required()
def delete_customers(customers_id):
    """
    Logic to delete customers data
    
    Parameter:
        customers_id (int): Id of the customers-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Customers.delete(customers_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
