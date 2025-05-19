
from flask import Blueprint, jsonify, request
from db import Products

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
    result = Products.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@products_bp.route('/<int:id>', methods=['PUT'])
def update_products(id):
    # Logic to update products data
    result = Products.update(request.values())
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
