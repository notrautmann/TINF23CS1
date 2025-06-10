"""
Implements the CRUD-operations for the ingredient_allergens-table.

Functions:

    get_ingredient_allergens(ingredient_allergens_id)
    create_ingredient_allergens()
    update_ingredient_allergens(ingredient_allergens_id)
    delete_ingredient_allergens(ingredient_allergens_id)

Misc variables:

    ingredient_allergens_id    
"""
    
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Ingredient_allergens

non_id_columns = ['ingredient_id',
	'allergen_id']

ingredient_allergens_bp = Blueprint('ingredient_allergens',
    __name__,
    url_prefix='/ingredient_allergens')

@ingredient_allergens_bp.route('/<int:ingredient_allergens_id>', methods=['GET'])
@jwt_required()
def get_ingredient_allergens(ingredient_allergens_id):
    """
    Logic to get ingredient_allergens data
    
    Parameter:
    ingredient_allergens_id (int): Id of the ingredient_allergens-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Ingredient_allergens.read(ingredient_allergens_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@ingredient_allergens_bp.route('/', methods=['POST'])
@jwt_required()
def create_ingredient_allergens():
    """
    Logic to create ingredient_allergens data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Ingredient_allergens.create(ingredient_id=request.values.get('ingredient_id'),
		allergen_id=request.values.get('allergen_id'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@ingredient_allergens_bp.route('/<int:ingredient_allergens_id>', methods=['PUT'])
@jwt_required()
def update_ingredient_allergens(ingredient_allergens_id):
    """
    Logic to update ingredient_allergens data
    
    Parameter:
        ingredient_allergens_id (int): Id of the ingredient_allergens-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Ingredient_allergens.update(ingredient_allergens_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@ingredient_allergens_bp.route('/<int:ingredient_allergens_id>', methods=['DELETE'])
@jwt_required()
def delete_ingredient_allergens(ingredient_allergens_id):
    """
    Logic to delete ingredient_allergens data
    
    Parameter:
        ingredient_allergens_id (int): Id of the ingredient_allergens-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Ingredient_allergens.delete(ingredient_allergens_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
