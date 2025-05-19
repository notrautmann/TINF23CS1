
from flask import Blueprint, jsonify, request
from db import Employee_time_entries

employee_time_entries_bp = Blueprint('employee_time_entries', __name__, url_prefix='/employee_time_entries')

@employee_time_entries_bp.route('/<int:id>', methods=['GET'])
def get_employee_time_entries(id):
    # Logic to get employee_time_entries data
    result = Employee_time_entries.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@employee_time_entries_bp.route('/', methods=['POST'])
def create_employee_time_entries():
    # Logic to create employee_time_entries data
    result = Employee_time_entries.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@employee_time_entries_bp.route('/<int:id>', methods=['PUT'])
def update_employee_time_entries(id):
    # Logic to update employee_time_entries data
    result = Employee_time_entries.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@employee_time_entries_bp.route('/<int:id>', methods=['DELETE'])
def delete_employee_time_entries(id):
    # Logic to delete employee_time_entries data
    result = Employee_time_entries.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
