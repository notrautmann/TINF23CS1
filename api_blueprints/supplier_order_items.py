
from flask import Blueprint, jsonify, request
from db import Supplier_order_items

supplier_order_items_bp = Blueprint('supplier_order_items', __name__, url_prefix='/supplier_order_items')

@supplier_order_items_bp.route('/<int:id>', methods=['GET'])
def get_supplier_order_items(id):
    # Logic to get supplier_order_items data
    result = Supplier_order_items.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@supplier_order_items_bp.route('/', methods=['POST'])
def create_supplier_order_items():
    # Logic to create supplier_order_items data
    result = Supplier_order_items.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_order_items_bp.route('/<int:id>', methods=['PUT'])
def update_supplier_order_items(id):
    # Logic to update supplier_order_items data
    result = Supplier_order_items.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_order_items_bp.route('/<int:id>', methods=['DELETE'])
def delete_supplier_order_items(id):
    # Logic to delete supplier_order_items data
    result = Supplier_order_items.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
