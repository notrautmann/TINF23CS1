"""
Implements the CRUD-operations for the machines-table.

Functions:

    get_machines(machines_id)
    create_machines()
    update_machines(machines_id)
    delete_machines(machines_id)

Misc variables:

    machines_id    
"""
    
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Machines

non_id_columns = ['branch_id',
	'name',
	'serial_number',
	'purchase_date',
	'last_maintenance']

machines_bp = Blueprint('machines',
    __name__,
    url_prefix='/machines')

@machines_bp.route('/<int:machines_id>', methods=['GET'])
@jwt_required()
def get_machines(machines_id):
    """
    Logic to get machines data
    
    Parameter:
    machines_id (int): Id of the machines-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Machines.read(machines_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@machines_bp.route('/', methods=['POST'])
@jwt_required()
def create_machines():
    """
    Logic to create machines data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Machines.create(branch_id=request.values.get('branch_id'),
		name=request.values.get('name'),
		serial_number=request.values.get('serial_number'),
		purchase_date=request.values.get('purchase_date'),
		last_maintenance=request.values.get('last_maintenance'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@machines_bp.route('/<int:machines_id>', methods=['PUT'])
@jwt_required()
def update_machines(machines_id):
    """
    Logic to update machines data
    
    Parameter:
        machines_id (int): Id of the machines-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Machines.update(machines_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@machines_bp.route('/<int:machines_id>', methods=['DELETE'])
@jwt_required()
def delete_machines(machines_id):
    """
    Logic to delete machines data
    
    Parameter:
        machines_id (int): Id of the machines-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Machines.delete(machines_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
