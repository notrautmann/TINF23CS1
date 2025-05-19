
from flask import Blueprint, jsonify, request
from db import Shifts

shifts_bp = Blueprint('shifts', __name__, url_prefix='/shifts')

@shifts_bp.route('/<int:id>', methods=['GET'])
def get_shifts(id):
    # Logic to get shifts data
    result = Shifts.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@shifts_bp.route('/', methods=['POST'])
def create_shifts():
    # Logic to create shifts data
    result = Shifts.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@shifts_bp.route('/<int:id>', methods=['PUT'])
def update_shifts(id):
    # Logic to update shifts data
    result = Shifts.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@shifts_bp.route('/<int:id>', methods=['DELETE'])
def delete_shifts(id):
    # Logic to delete shifts data
    result = Shifts.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
