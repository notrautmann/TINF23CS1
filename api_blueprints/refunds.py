
from flask import Blueprint, jsonify, request
from db import Refunds

refunds_bp = Blueprint('refunds', __name__, url_prefix='/refunds')

@refunds_bp.route('/<int:id>', methods=['GET'])
def get_refunds(id):
    # Logic to get refunds data
    result = Refunds.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@refunds_bp.route('/', methods=['POST'])
def create_refunds():
    # Logic to create refunds data
    result = Refunds.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@refunds_bp.route('/<int:id>', methods=['PUT'])
def update_refunds(id):
    # Logic to update refunds data
    result = Refunds.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@refunds_bp.route('/<int:id>', methods=['DELETE'])
def delete_refunds(id):
    # Logic to delete refunds data
    result = Refunds.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
