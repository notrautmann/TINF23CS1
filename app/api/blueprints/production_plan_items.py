"""
Implements the CRUD-operations for the production_plan_items-table.

Functions:

    get_production_plan_items(production_plan_items_id)
    create_production_plan_items()
    update_production_plan_items(production_plan_items_id)
    delete_production_plan_items(production_plan_items_id)

Misc variables:

    production_plan_items_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.records.production_plan_items import Production_plan_items

non_id_columns = ['plan_id',
	'product_id',
	'planned_qty',
	'produced_qty']

production_plan_items_bp = Blueprint('production_plan_items',
    __name__,
    url_prefix='/production_plan_items')

@production_plan_items_bp.route('/<int:production_plan_items_id>', methods=['GET'])
@jwt_required()
def get_production_plan_items(production_plan_items_id):
    """
    Logic to get production_plan_items data
    
    Parameter:
    production_plan_items_id (int): Id of the production_plan_items-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Production_plan_items.read(production_plan_items_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@production_plan_items_bp.route('/', methods=['POST'])
@jwt_required()
def create_production_plan_items():
    """
    Logic to create production_plan_items data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Production_plan_items.create(plan_id=request.values.get('plan_id'),
		product_id=request.values.get('product_id'),
		planned_qty=request.values.get('planned_qty'),
		produced_qty=request.values.get('produced_qty'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@production_plan_items_bp.route('/<int:production_plan_items_id>', methods=['PUT'])
@jwt_required()
def update_production_plan_items(production_plan_items_id):
    """
    Logic to update production_plan_items data
    
    Parameter:
        production_plan_items_id (int): Id of the production_plan_items-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Production_plan_items.update(production_plan_items_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@production_plan_items_bp.route('/<int:production_plan_items_id>', methods=['DELETE'])
@jwt_required()
def delete_production_plan_items(production_plan_items_id):
    """
    Logic to delete production_plan_items data
    
    Parameter:
        production_plan_items_id (int): Id of the production_plan_items-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Production_plan_items.delete(production_plan_items_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
