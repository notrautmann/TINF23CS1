
from flask import Blueprint, jsonify, request
from db import Complaints

non_id_columns = ['customer_id', 'order_id', 'product_id', 'description', 'resolved', 'created_at', 'resolved_at']

complaints_bp = Blueprint('complaints', __name__, url_prefix='/complaints')

@complaints_bp.route('/<int:id>', methods=['GET'])
def get_complaints(id):
    # Logic to get complaints data
    result = Complaints.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@complaints_bp.route('/', methods=['POST'])
def create_complaints():
    # Logic to create complaints data
    result = Complaints.create(customer_id=request.values.get('customer_id'), order_id=request.values.get('order_id'), product_id=request.values.get('product_id'), description=request.values.get('description'), resolved=request.values.get('resolved'), created_at=request.values.get('created_at'), resolved_at=request.values.get('resolved_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@complaints_bp.route('/<int:id>', methods=['PUT'])
def update_complaints(id):
    # Logic to update complaints data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Complaints.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@complaints_bp.route('/<int:id>', methods=['DELETE'])
def delete_complaints(id):
    # Logic to delete complaints data
    result = Complaints.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
