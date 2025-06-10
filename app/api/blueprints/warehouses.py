"""
Implements the CRUD-operations for the warehouses-table.

Functions:

    get_warehouses(warehouses_id)
    create_warehouses()
    update_warehouses(warehouses_id)
    delete_warehouses(warehouses_id)

Misc variables:

    warehouses_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.records.warehouses import Warehouses

non_id_columns = ['branch_id',
	'name',
	'description']

warehouses_bp = Blueprint('warehouses',
    __name__,
    url_prefix='/warehouses')

@warehouses_bp.route('/<int:warehouses_id>', methods=['GET'])
@jwt_required()
def get_warehouses(warehouses_id):
    """
    Logic to get warehouses data
    
    Parameter:
    warehouses_id (int): Id of the warehouses-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Warehouses.read(warehouses_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@warehouses_bp.route('/', methods=['POST'])
@jwt_required()
def create_warehouses():
    """
    Logic to create warehouses data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Warehouses.create(branch_id=request.values.get('branch_id'),
		name=request.values.get('name'),
		description=request.values.get('description'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@warehouses_bp.route('/<int:warehouses_id>', methods=['PUT'])
@jwt_required()
def update_warehouses(warehouses_id):
    """
    Logic to update warehouses data
    
    Parameter:
        warehouses_id (int): Id of the warehouses-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Warehouses.update(warehouses_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@warehouses_bp.route('/<int:warehouses_id>', methods=['DELETE'])
@jwt_required()
def delete_warehouses(warehouses_id):
    """
    Logic to delete warehouses data
    
    Parameter:
        warehouses_id (int): Id of the warehouses-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Warehouses.delete(warehouses_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
