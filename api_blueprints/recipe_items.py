
from flask import Blueprint, jsonify, request
from db import Recipe_items

non_id_columns = ['recipe_id', 'ingredient_id', 'quantity', 'unit']

recipe_items_bp = Blueprint('recipe_items', __name__, url_prefix='/recipe_items')

@recipe_items_bp.route('/<int:id>', methods=['GET'])
def get_recipe_items(id):
    # Logic to get recipe_items data
    result = Recipe_items.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@recipe_items_bp.route('/', methods=['POST'])
def create_recipe_items():
    # Logic to create recipe_items data
    result = Recipe_items.create(recipe_id=request.values.get('recipe_id'), ingredient_id=request.values.get('ingredient_id'), quantity=request.values.get('quantity'), unit=request.values.get('unit'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@recipe_items_bp.route('/<int:id>', methods=['PUT'])
def update_recipe_items(id):
    # Logic to update recipe_items data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Recipe_items.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@recipe_items_bp.route('/<int:id>', methods=['DELETE'])
def delete_recipe_items(id):
    # Logic to delete recipe_items data
    result = Recipe_items.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
