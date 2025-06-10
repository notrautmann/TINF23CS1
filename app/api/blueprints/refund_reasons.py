"""
Implements the CRUD-operations for the refund_reasons-table.

Functions:

    get_refund_reasons(refund_reasons_id)
    create_refund_reasons()
    update_refund_reasons(refund_reasons_id)
    delete_refund_reasons(refund_reasons_id)

Misc variables:

    refund_reasons_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.records.refund_reasons import Refund_reasons

non_id_columns = ['code',
	'description']

refund_reasons_bp = Blueprint('refund_reasons',
    __name__,
    url_prefix='/refund_reasons')

@refund_reasons_bp.route('/<int:refund_reasons_id>', methods=['GET'])
@jwt_required()
def get_refund_reasons(refund_reasons_id):
    """
    Logic to get refund_reasons data
    
    Parameter:
    refund_reasons_id (int): Id of the refund_reasons-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Refund_reasons.read(refund_reasons_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@refund_reasons_bp.route('/', methods=['POST'])
@jwt_required()
def create_refund_reasons():
    """
    Logic to create refund_reasons data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Refund_reasons.create(code=request.values.get('code'),
		description=request.values.get('description'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@refund_reasons_bp.route('/<int:refund_reasons_id>', methods=['PUT'])
@jwt_required()
def update_refund_reasons(refund_reasons_id):
    """
    Logic to update refund_reasons data
    
    Parameter:
        refund_reasons_id (int): Id of the refund_reasons-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Refund_reasons.update(refund_reasons_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@refund_reasons_bp.route('/<int:refund_reasons_id>', methods=['DELETE'])
@jwt_required()
def delete_refund_reasons(refund_reasons_id):
    """
    Logic to delete refund_reasons data
    
    Parameter:
        refund_reasons_id (int): Id of the refund_reasons-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Refund_reasons.delete(refund_reasons_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
