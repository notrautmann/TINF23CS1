
from flask import Blueprint, jsonify, request
from db import Ingredients

ingredients_bp = Blueprint('ingredients', __name__, url_prefix='/ingredients')

@ingredients_bp.route('/<int:id>', methods=['GET'])
def get_ingredients(id):
    # Logic to get ingredients data
    result = Ingredients.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@ingredients_bp.route('/', methods=['POST'])
def create_ingredients():
    # Logic to create ingredients data
    result = Ingredients.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@ingredients_bp.route('/<int:id>', methods=['PUT'])
def update_ingredients(id):
    # Logic to update ingredients data
    result = Ingredients.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@ingredients_bp.route('/<int:id>', methods=['DELETE'])
def delete_ingredients(id):
    # Logic to delete ingredients data
    result = Ingredients.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
