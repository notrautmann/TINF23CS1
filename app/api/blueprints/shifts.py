
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Shifts

non_id_columns = ['branch_id',
	'name',
	'start_time',
	'end_time']

shifts_bp = Blueprint('shifts',
    __name__,
    url_prefix='/shifts')

@shifts_bp.route('/<int:shifts_id>', methods=['GET'])
@jwt_required()
def get_shifts(shifts_id):
    # Logic to get shifts data
    result = Shifts.read(shifts_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@shifts_bp.route('/', methods=['POST'])
@jwt_required()
def create_shifts():
    # Logic to create shifts data
    result = Shifts.create(branch_id=request.values.get('branch_id'),
		name=request.values.get('name'),
		start_time=request.values.get('start_time'),
		end_time=request.values.get('end_time'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@shifts_bp.route('/<int:shifts_id>', methods=['PUT'])
@jwt_required()
def update_shifts(shifts_id):
    # Logic to update shifts data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Shifts.update(shifts_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@shifts_bp.route('/<int:shifts_id>', methods=['DELETE'])
@jwt_required()
def delete_shifts(shifts_id):
    # Logic to delete shifts data
    result = Shifts.delete(shifts_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
