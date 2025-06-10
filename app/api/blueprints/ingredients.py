"""
Implements the CRUD-operations for the ingredients-table.

Functions:

    get_ingredients(ingredients_id)
    create_ingredients()
    update_ingredients(ingredients_id)
    delete_ingredients(ingredients_id)

Misc variables:

    ingredients_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Ingredients

non_id_columns = ['name',
	'unit',
	'purchase_price',
	'tax_code_id',
	'is_active',
	'created_at',
	'updated_at']

ingredients_bp = Blueprint('ingredients',
    __name__,
    url_prefix='/ingredients')

@ingredients_bp.route('/<int:ingredients_id>', methods=['GET'])
@jwt_required()
def get_ingredients(ingredients_id):
    """
    Logic to get ingredients data
    
    Parameter:
    ingredients_id (int): Id of the ingredients-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Ingredients.read(ingredients_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@ingredients_bp.route('/', methods=['POST'])
@jwt_required()
def create_ingredients():
    """
    Logic to create ingredients data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Ingredients.create(name=request.values.get('name'),
		unit=request.values.get('unit'),
		purchase_price=request.values.get('purchase_price'),
		tax_code_id=request.values.get('tax_code_id'),
		is_active=request.values.get('is_active'),
		created_at=request.values.get('created_at'),
		updated_at=request.values.get('updated_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@ingredients_bp.route('/<int:ingredients_id>', methods=['PUT'])
@jwt_required()
def update_ingredients(ingredients_id):
    """
    Logic to update ingredients data
    
    Parameter:
        ingredients_id (int): Id of the ingredients-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Ingredients.update(ingredients_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@ingredients_bp.route('/<int:ingredients_id>', methods=['DELETE'])
@jwt_required()
def delete_ingredients(ingredients_id):
    """
    Logic to delete ingredients data
    
    Parameter:
        ingredients_id (int): Id of the ingredients-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Ingredients.delete(ingredients_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
