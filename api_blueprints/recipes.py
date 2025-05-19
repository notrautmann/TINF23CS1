
from flask import Blueprint, jsonify, request
from db import Recipes

recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route('/<int:id>', methods=['GET'])
def get_recipes(id):
    # Logic to get recipes data
    result = Recipes.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@recipes_bp.route('/', methods=['POST'])
def create_recipes():
    # Logic to create recipes data
    result = Recipes.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@recipes_bp.route('/<int:id>', methods=['PUT'])
def update_recipes(id):
    # Logic to update recipes data
    result = Recipes.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@recipes_bp.route('/<int:id>', methods=['DELETE'])
def delete_recipes(id):
    # Logic to delete recipes data
    result = Recipes.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
