
from flask import Blueprint, jsonify, request
from db import Machines

non_id_columns = ['branch_id', 'name', 'serial_number', 'purchase_date', 'last_maintenance']

machines_bp = Blueprint('machines', __name__, url_prefix='/machines')

@machines_bp.route('/<int:id>', methods=['GET'])
def get_machines(id):
    # Logic to get machines data
    result = Machines.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@machines_bp.route('/', methods=['POST'])
def create_machines():
    # Logic to create machines data
    result = Machines.create(branch_id=request.values.get('branch_id'), name=request.values.get('name'), serial_number=request.values.get('serial_number'), purchase_date=request.values.get('purchase_date'), last_maintenance=request.values.get('last_maintenance'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@machines_bp.route('/<int:id>', methods=['PUT'])
def update_machines(id):
    # Logic to update machines data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Machines.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@machines_bp.route('/<int:id>', methods=['DELETE'])
def delete_machines(id):
    # Logic to delete machines data
    result = Machines.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
