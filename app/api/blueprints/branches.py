"""
Implements the CRUD-operations for the branches-table.

Functions:

    get_branches(branches_id)
    create_branches()
    update_branches(branches_id)
    delete_branches(branches_id)

Misc variables:

    branches_id    
"""
    
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Branches

non_id_columns = ['name',
	'address_line',
	'postal_code',
	'city',
	'country',
	'phone',
	'email',
	'opening_note',
	'created_at',
	'updated_at']

branches_bp = Blueprint('branches',
    __name__,
    url_prefix='/branches')

@branches_bp.route('/<int:branches_id>', methods=['GET'])
@jwt_required()
def get_branches(branches_id):
    """
    Logic to get branches data
    
    Parameter:
    branches_id (int): Id of the branches-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Branches.read(branches_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@branches_bp.route('/', methods=['POST'])
@jwt_required()
def create_branches():
    """
    Logic to create branches data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Branches.create(name=request.values.get('name'),
		address_line=request.values.get('address_line'),
		postal_code=request.values.get('postal_code'),
		city=request.values.get('city'),
		country=request.values.get('country'),
		phone=request.values.get('phone'),
		email=request.values.get('email'),
		opening_note=request.values.get('opening_note'),
		created_at=request.values.get('created_at'),
		updated_at=request.values.get('updated_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@branches_bp.route('/<int:branches_id>', methods=['PUT'])
@jwt_required()
def update_branches(branches_id):
    """
    Logic to update branches data
    
    Parameter:
        branches_id (int): Id of the branches-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Branches.update(branches_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@branches_bp.route('/<int:branches_id>', methods=['DELETE'])
@jwt_required()
def delete_branches(branches_id):
    """
    Logic to delete branches data
    
    Parameter:
        branches_id (int): Id of the branches-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Branches.delete(branches_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
