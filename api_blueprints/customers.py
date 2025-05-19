
from flask import Blueprint, jsonify, request
from db import Customers

customers_bp = Blueprint('customers', __name__, url_prefix='/customers')

@customers_bp.route('/<int:id>', methods=['GET'])
def get_customers(id):
    # Logic to get customers data
    result = Customers.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@customers_bp.route('/', methods=['POST'])
def create_customers():
    # Logic to create customers data
    result = Customers.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customers_bp.route('/<int:id>', methods=['PUT'])
def update_customers(id):
    # Logic to update customers data
    result = Customers.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customers_bp.route('/<int:id>', methods=['DELETE'])
def delete_customers(id):
    # Logic to delete customers data
    result = Customers.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
