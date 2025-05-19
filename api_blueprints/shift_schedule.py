
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from db import Shift_schedule

non_id_columns = ['shift_id', 'employee_id', 'schedule_date', 'assigned_hours']

shift_schedule_bp = Blueprint('shift_schedule', __name__, url_prefix='/shift_schedule')

@shift_schedule_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_shift_schedule(id):
    # Logic to get shift_schedule data
    result = Shift_schedule.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@shift_schedule_bp.route('/', methods=['POST'])
@jwt_required()
def create_shift_schedule():
    # Logic to create shift_schedule data
    result = Shift_schedule.create(shift_id=request.values.get('shift_id'), employee_id=request.values.get('employee_id'), schedule_date=request.values.get('schedule_date'), assigned_hours=request.values.get('assigned_hours'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@shift_schedule_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_shift_schedule(id):
    # Logic to update shift_schedule data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Shift_schedule.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@shift_schedule_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_shift_schedule(id):
    # Logic to delete shift_schedule data
    result = Shift_schedule.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
