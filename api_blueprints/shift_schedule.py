
from flask import Blueprint, jsonify, request
from db import Shift_schedule

shift_schedule_bp = Blueprint('shift_schedule', __name__, url_prefix='/shift_schedule')

@shift_schedule_bp.route('/<int:id>', methods=['GET'])
def get_shift_schedule(id):
    # Logic to get shift_schedule data
    result = Shift_schedule.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@shift_schedule_bp.route('/', methods=['POST'])
def create_shift_schedule():
    # Logic to create shift_schedule data
    result = Shift_schedule.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@shift_schedule_bp.route('/<int:id>', methods=['PUT'])
def update_shift_schedule(id):
    # Logic to update shift_schedule data
    result = Shift_schedule.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@shift_schedule_bp.route('/<int:id>', methods=['DELETE'])
def delete_shift_schedule(id):
    # Logic to delete shift_schedule data
    result = Shift_schedule.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
