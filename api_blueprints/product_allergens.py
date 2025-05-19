
from flask import Blueprint, jsonify, request
from db import Product_allergens

non_id_columns = ['product_id', 'allergen_id']

product_allergens_bp = Blueprint('product_allergens', __name__, url_prefix='/product_allergens')

@product_allergens_bp.route('/<int:id>', methods=['GET'])
def get_product_allergens(id):
    # Logic to get product_allergens data
    result = Product_allergens.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@product_allergens_bp.route('/', methods=['POST'])
def create_product_allergens():
    # Logic to create product_allergens data
    result = Product_allergens.create(product_id=request.values.get('product_id'), allergen_id=request.values.get('allergen_id'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@product_allergens_bp.route('/<int:id>', methods=['PUT'])
def update_product_allergens(id):
    # Logic to update product_allergens data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Product_allergens.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@product_allergens_bp.route('/<int:id>', methods=['DELETE'])
def delete_product_allergens(id):
    # Logic to delete product_allergens data
    result = Product_allergens.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
