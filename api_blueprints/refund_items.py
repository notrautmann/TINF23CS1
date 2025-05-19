
from flask import Blueprint, jsonify, request
from db import Refund_items

refund_items_bp = Blueprint('refund_items', __name__, url_prefix='/refund_items')

@refund_items_bp.route('/<int:id>', methods=['GET'])
def get_refund_items(id):
    # Logic to get refund_items data
    result = Refund_items.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@refund_items_bp.route('/', methods=['POST'])
def create_refund_items():
    # Logic to create refund_items data
    result = Refund_items.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@refund_items_bp.route('/<int:id>', methods=['PUT'])
def update_refund_items(id):
    # Logic to update refund_items data
    result = Refund_items.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@refund_items_bp.route('/<int:id>', methods=['DELETE'])
def delete_refund_items(id):
    # Logic to delete refund_items data
    result = Refund_items.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
