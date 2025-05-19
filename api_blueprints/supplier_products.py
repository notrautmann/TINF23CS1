
from flask import Blueprint, jsonify, request
from db import Supplier_products

supplier_products_bp = Blueprint('supplier_products', __name__, url_prefix='/supplier_products')

@supplier_products_bp.route('/<int:id>', methods=['GET'])
def get_supplier_products(id):
    # Logic to get supplier_products data
    result = Supplier_products.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@supplier_products_bp.route('/', methods=['POST'])
def create_supplier_products():
    # Logic to create supplier_products data
    result = Supplier_products.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_products_bp.route('/<int:id>', methods=['PUT'])
def update_supplier_products(id):
    # Logic to update supplier_products data
    result = Supplier_products.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_products_bp.route('/<int:id>', methods=['DELETE'])
def delete_supplier_products(id):
    # Logic to delete supplier_products data
    result = Supplier_products.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
