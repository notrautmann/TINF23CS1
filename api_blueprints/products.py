
from flask import Blueprint, jsonify, request
from db import Products

non_id_columns = ['name', 'sku', 'recipe_id', 'sales_price', 'tax_code_id', 'is_active', 'created_at', 'updated_at']

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/<int:id>', methods=['GET'])
def get_products(id):
    # Logic to get products data
    result = Products.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@products_bp.route('/', methods=['POST'])
def create_products():
    # Logic to create products data
    result = Products.create(name=request.values.get('name'), sku=request.values.get('sku'), recipe_id=request.values.get('recipe_id'), sales_price=request.values.get('sales_price'), tax_code_id=request.values.get('tax_code_id'), is_active=request.values.get('is_active'), created_at=request.values.get('created_at'), updated_at=request.values.get('updated_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@products_bp.route('/<int:id>', methods=['PUT'])
def update_products(id):
    # Logic to update products data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Products.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@products_bp.route('/<int:id>', methods=['DELETE'])
def delete_products(id):
    # Logic to delete products data
    result = Products.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
