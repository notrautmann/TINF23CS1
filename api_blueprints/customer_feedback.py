
from flask import Blueprint, jsonify, request
from db import Customer_feedback

customer_feedback_bp = Blueprint('customer_feedback', __name__, url_prefix='/customer_feedback')

@customer_feedback_bp.route('/<int:id>', methods=['GET'])
def get_customer_feedback(id):
    # Logic to get customer_feedback data
    result = Customer_feedback.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@customer_feedback_bp.route('/', methods=['POST'])
def create_customer_feedback():
    # Logic to create customer_feedback data
    result = Customer_feedback.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_feedback_bp.route('/<int:id>', methods=['PUT'])
def update_customer_feedback(id):
    # Logic to update customer_feedback data
    result = Customer_feedback.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_feedback_bp.route('/<int:id>', methods=['DELETE'])
def delete_customer_feedback(id):
    # Logic to delete customer_feedback data
    result = Customer_feedback.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
