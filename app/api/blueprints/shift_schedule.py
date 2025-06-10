"""
Implements the CRUD-operations for the shift_schedule-table.

Functions:

    get_shift_schedule(shift_schedule_id)
    create_shift_schedule()
    update_shift_schedule(shift_schedule_id)
    delete_shift_schedule(shift_schedule_id)

Misc variables:

    shift_schedule_id    
"""
    
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Shift_schedule

non_id_columns = ['shift_id',
	'employee_id',
	'schedule_date',
	'assigned_hours']

shift_schedule_bp = Blueprint('shift_schedule',
    __name__,
    url_prefix='/shift_schedule')

@shift_schedule_bp.route('/<int:shift_schedule_id>', methods=['GET'])
@jwt_required()
def get_shift_schedule(shift_schedule_id):
    """
    Logic to get shift_schedule data
    
    Parameter:
    shift_schedule_id (int): Id of the shift_schedule-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Shift_schedule.read(shift_schedule_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@shift_schedule_bp.route('/', methods=['POST'])
@jwt_required()
def create_shift_schedule():
    """
    Logic to create shift_schedule data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Shift_schedule.create(shift_id=request.values.get('shift_id'),
		employee_id=request.values.get('employee_id'),
		schedule_date=request.values.get('schedule_date'),
		assigned_hours=request.values.get('assigned_hours'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@shift_schedule_bp.route('/<int:shift_schedule_id>', methods=['PUT'])
@jwt_required()
def update_shift_schedule(shift_schedule_id):
    """
    Logic to update shift_schedule data
    
    Parameter:
        shift_schedule_id (int): Id of the shift_schedule-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Shift_schedule.update(shift_schedule_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@shift_schedule_bp.route('/<int:shift_schedule_id>', methods=['DELETE'])
@jwt_required()
def delete_shift_schedule(shift_schedule_id):
    """
    Logic to delete shift_schedule data
    
    Parameter:
        shift_schedule_id (int): Id of the shift_schedule-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Shift_schedule.delete(shift_schedule_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
