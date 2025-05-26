
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Customer_feedback

non_id_columns = ['customer_id', 'branch_id', 'order_id', 'rating', 'comment', 'created_at']

customer_feedback_bp = Blueprint('customer_feedback', __name__, url_prefix='/customer_feedback')

@customer_feedback_bp.route('/<int:customer_feedback_id>', methods=['GET'])
@jwt_required()
def get_customer_feedback(customer_feedback_id):
    # Logic to get customer_feedback data
    result = Customer_feedback.read(customer_feedback_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@customer_feedback_bp.route('/', methods=['POST'])
@jwt_required()
def create_customer_feedback():
    # Logic to create customer_feedback data
    result = Customer_feedback.create(customer_id=request.values.get('customer_id'), branch_id=request.values.get('branch_id'), order_id=request.values.get('order_id'), rating=request.values.get('rating'), comment=request.values.get('comment'), created_at=request.values.get('created_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_feedback_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_customer_feedback(id):
    # Logic to update customer_feedback data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Customer_feedback.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_feedback_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_customer_feedback(id):
    # Logic to delete customer_feedback data
    result = Customer_feedback.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
