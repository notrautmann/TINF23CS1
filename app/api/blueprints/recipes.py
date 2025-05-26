
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Recipes

non_id_columns = ['name', 'description', 'created_at', 'updated_at']

recipes_bp = Blueprint('recipes', __name__, url_prefix='/recipes')

@recipes_bp.route('/<int:recipes_id>', methods=['GET'])
@jwt_required()
def get_recipes(recipes_id):
    # Logic to get recipes data
    result = Recipes.read(recipes_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@recipes_bp.route('/', methods=['POST'])
@jwt_required()
def create_recipes():
    # Logic to create recipes data
    result = Recipes.create(name=request.values.get('name'), description=request.values.get('description'), created_at=request.values.get('created_at'), updated_at=request.values.get('updated_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@recipes_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_recipes(id):
    # Logic to update recipes data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Recipes.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@recipes_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_recipes(id):
    # Logic to delete recipes data
    result = Recipes.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
