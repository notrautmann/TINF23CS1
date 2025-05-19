
from flask import Blueprint, jsonify, request
from db import Ingredient_allergens

ingredient_allergens_bp = Blueprint('ingredient_allergens', __name__, url_prefix='/ingredient_allergens')

@ingredient_allergens_bp.route('/<int:id>', methods=['GET'])
def get_ingredient_allergens(id):
    # Logic to get ingredient_allergens data
    result = Ingredient_allergens.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@ingredient_allergens_bp.route('/', methods=['POST'])
def create_ingredient_allergens():
    # Logic to create ingredient_allergens data
    result = Ingredient_allergens.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@ingredient_allergens_bp.route('/<int:id>', methods=['PUT'])
def update_ingredient_allergens(id):
    # Logic to update ingredient_allergens data
    result = Ingredient_allergens.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@ingredient_allergens_bp.route('/<int:id>', methods=['DELETE'])
def delete_ingredient_allergens(id):
    # Logic to delete ingredient_allergens data
    result = Ingredient_allergens.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
