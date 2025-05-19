
from flask import Blueprint, jsonify, request
from db import Customer_orders

customer_orders_bp = Blueprint('customer_orders', __name__, url_prefix='/customer_orders')

@customer_orders_bp.route('/<int:id>', methods=['GET'])
def get_customer_orders(id):
    # Logic to get customer_orders data
    result = Customer_orders.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@customer_orders_bp.route('/', methods=['POST'])
def create_customer_orders():
    # Logic to create customer_orders data
    result = Customer_orders.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_orders_bp.route('/<int:id>', methods=['PUT'])
def update_customer_orders(id):
    # Logic to update customer_orders data
    result = Customer_orders.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_orders_bp.route('/<int:id>', methods=['DELETE'])
def delete_customer_orders(id):
    # Logic to delete customer_orders data
    result = Customer_orders.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
