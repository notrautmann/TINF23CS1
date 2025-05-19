
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from db import Ingredient_allergens

non_id_columns = ['ingredient_id', 'allergen_id']

ingredient_allergens_bp = Blueprint('ingredient_allergens', __name__, url_prefix='/ingredient_allergens')

@ingredient_allergens_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_ingredient_allergens(id):
    # Logic to get ingredient_allergens data
    result = Ingredient_allergens.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@ingredient_allergens_bp.route('/', methods=['POST'])
@jwt_required()
def create_ingredient_allergens():
    # Logic to create ingredient_allergens data
    result = Ingredient_allergens.create(ingredient_id=request.values.get('ingredient_id'), allergen_id=request.values.get('allergen_id'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@ingredient_allergens_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_ingredient_allergens(id):
    # Logic to update ingredient_allergens data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Ingredient_allergens.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@ingredient_allergens_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_ingredient_allergens(id):
    # Logic to delete ingredient_allergens data
    result = Ingredient_allergens.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
