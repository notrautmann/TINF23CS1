
from flask import Blueprint, jsonify, request
from db import Ingredients

non_id_columns = ['name', 'unit', 'purchase_price', 'tax_code_id', 'is_active', 'created_at', 'updated_at']

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
    result = Ingredients.create(name=request.values.get('name'), unit=request.values.get('unit'), purchase_price=request.values.get('purchase_price'), tax_code_id=request.values.get('tax_code_id'), is_active=request.values.get('is_active'), created_at=request.values.get('created_at'), updated_at=request.values.get('updated_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@ingredients_bp.route('/<int:id>', methods=['PUT'])
def update_ingredients(id):
    # Logic to update ingredients data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Ingredients.update(id, **changes)
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
