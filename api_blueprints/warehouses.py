
from flask import Blueprint, jsonify, request
from db import Warehouses

warehouses_bp = Blueprint('warehouses', __name__, url_prefix='/warehouses')

@warehouses_bp.route('/<int:id>', methods=['GET'])
def get_warehouses(id):
    # Logic to get warehouses data
    result = Warehouses.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@warehouses_bp.route('/', methods=['POST'])
def create_warehouses():
    # Logic to create warehouses data
    result = Warehouses.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@warehouses_bp.route('/<int:id>', methods=['PUT'])
def update_warehouses(id):
    # Logic to update warehouses data
    result = Warehouses.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@warehouses_bp.route('/<int:id>', methods=['DELETE'])
def delete_warehouses(id):
    # Logic to delete warehouses data
    result = Warehouses.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
