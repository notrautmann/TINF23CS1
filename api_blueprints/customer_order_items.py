
from flask import Blueprint, jsonify, request
from db import Customer_order_items

customer_order_items_bp = Blueprint('customer_order_items', __name__, url_prefix='/customer_order_items')

@customer_order_items_bp.route('/<int:id>', methods=['GET'])
def get_customer_order_items(id):
    # Logic to get customer_order_items data
    result = Customer_order_items.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@customer_order_items_bp.route('/', methods=['POST'])
def create_customer_order_items():
    # Logic to create customer_order_items data
    result = Customer_order_items.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_order_items_bp.route('/<int:id>', methods=['PUT'])
def update_customer_order_items(id):
    # Logic to update customer_order_items data
    result = Customer_order_items.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_order_items_bp.route('/<int:id>', methods=['DELETE'])
def delete_customer_order_items(id):
    # Logic to delete customer_order_items data
    result = Customer_order_items.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
