
from flask import Blueprint, jsonify, request
from db import Supplier_orders

supplier_orders_bp = Blueprint('supplier_orders', __name__, url_prefix='/supplier_orders')

@supplier_orders_bp.route('/<int:id>', methods=['GET'])
def get_supplier_orders(id):
    # Logic to get supplier_orders data
    result = Supplier_orders.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@supplier_orders_bp.route('/', methods=['POST'])
def create_supplier_orders():
    # Logic to create supplier_orders data
    result = Supplier_orders.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_orders_bp.route('/<int:id>', methods=['PUT'])
def update_supplier_orders(id):
    # Logic to update supplier_orders data
    result = Supplier_orders.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_orders_bp.route('/<int:id>', methods=['DELETE'])
def delete_supplier_orders(id):
    # Logic to delete supplier_orders data
    result = Supplier_orders.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
