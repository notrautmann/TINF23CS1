
from flask import Blueprint, jsonify, request
from db import Refund_reasons

refund_reasons_bp = Blueprint('refund_reasons', __name__, url_prefix='/refund_reasons')

@refund_reasons_bp.route('/<int:id>', methods=['GET'])
def get_refund_reasons(id):
    # Logic to get refund_reasons data
    result = Refund_reasons.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@refund_reasons_bp.route('/', methods=['POST'])
def create_refund_reasons():
    # Logic to create refund_reasons data
    result = Refund_reasons.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@refund_reasons_bp.route('/<int:id>', methods=['PUT'])
def update_refund_reasons(id):
    # Logic to update refund_reasons data
    result = Refund_reasons.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@refund_reasons_bp.route('/<int:id>', methods=['DELETE'])
def delete_refund_reasons(id):
    # Logic to delete refund_reasons data
    result = Refund_reasons.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
