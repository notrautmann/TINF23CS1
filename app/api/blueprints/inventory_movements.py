"""
Implements the CRUD-operations for the inventory_movements-table.

Functions:

    get_inventory_movements(inventory_movements_id)
    create_inventory_movements()
    update_inventory_movements(inventory_movements_id)
    delete_inventory_movements(inventory_movements_id)

Misc variables:

    inventory_movements_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Inventory_movements

non_id_columns = ['movement_type',
	'ingredient_id',
	'qty',
	'unit',
	'from_location_id',
	'to_location_id',
	'reference_type',
	'reference_id',
	'created_at',
	'user_id']

inventory_movements_bp = Blueprint('inventory_movements',
    __name__,
    url_prefix='/inventory_movements')

@inventory_movements_bp.route('/<int:inventory_movements_id>', methods=['GET'])
@jwt_required()
def get_inventory_movements(inventory_movements_id):
    """
    Logic to get inventory_movements data
    
    Parameter:
    inventory_movements_id (int): Id of the inventory_movements-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Inventory_movements.read(inventory_movements_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@inventory_movements_bp.route('/', methods=['POST'])
@jwt_required()
def create_inventory_movements():
    """
    Logic to create inventory_movements data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Inventory_movements.create(movement_type=request.values.get('movement_type'),
		ingredient_id=request.values.get('ingredient_id'),
		qty=request.values.get('qty'),
		unit=request.values.get('unit'),
		from_location_id=request.values.get('from_location_id'),
		to_location_id=request.values.get('to_location_id'),
		reference_type=request.values.get('reference_type'),
		reference_id=request.values.get('reference_id'),
		created_at=request.values.get('created_at'),
		user_id=request.values.get('user_id'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@inventory_movements_bp.route('/<int:inventory_movements_id>', methods=['PUT'])
@jwt_required()
def update_inventory_movements(inventory_movements_id):
    """
    Logic to update inventory_movements data
    
    Parameter:
        inventory_movements_id (int): Id of the inventory_movements-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Inventory_movements.update(inventory_movements_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@inventory_movements_bp.route('/<int:inventory_movements_id>', methods=['DELETE'])
@jwt_required()
def delete_inventory_movements(inventory_movements_id):
    """
    Logic to delete inventory_movements data
    
    Parameter:
        inventory_movements_id (int): Id of the inventory_movements-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Inventory_movements.delete(inventory_movements_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
