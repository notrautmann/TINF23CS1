
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Employee_time_entries

non_id_columns = ['employee_id',
	'branch_id',
	'clock_in',
	'clock_out',
	'break_minutes']

employee_time_entries_bp = Blueprint('employee_time_entries',
    __name__,
    url_prefix='/employee_time_entries')

@employee_time_entries_bp.route('/<int:employee_time_entries_id>', methods=['GET'])
@jwt_required()
def get_employee_time_entries(employee_time_entries_id):
    # Logic to get employee_time_entries data
    result = Employee_time_entries.read(employee_time_entries_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@employee_time_entries_bp.route('/', methods=['POST'])
@jwt_required()
def create_employee_time_entries():
    # Logic to create employee_time_entries data
    result = Employee_time_entries.create(employee_id=request.values.get('employee_id'),
		branch_id=request.values.get('branch_id'),
		clock_in=request.values.get('clock_in'),
		clock_out=request.values.get('clock_out'),
		break_minutes=request.values.get('break_minutes'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@employee_time_entries_bp.route('/<int:employee_time_entries_id>', methods=['PUT'])
@jwt_required()
def update_employee_time_entries(employee_time_entries_id):
    # Logic to update employee_time_entries data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Employee_time_entries.update(employee_time_entries_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@employee_time_entries_bp.route('/<int:employee_time_entries_id>', methods=['DELETE'])
@jwt_required()
def delete_employee_time_entries(employee_time_entries_id):
    # Logic to delete employee_time_entries data
    result = Employee_time_entries.delete(employee_time_entries_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
