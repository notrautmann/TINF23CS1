"""
Implements the CRUD-operations for the complaints-table.

Functions:

    get_complaints(complaints_id)
    create_complaints()
    update_complaints(complaints_id)
    delete_complaints(complaints_id)

Misc variables:

    complaints_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Complaints

non_id_columns = ['customer_id',
	'order_id',
	'product_id',
	'description',
	'resolved',
	'created_at',
	'resolved_at']

complaints_bp = Blueprint('complaints',
    __name__,
    url_prefix='/complaints')

@complaints_bp.route('/<int:complaints_id>', methods=['GET'])
@jwt_required()
def get_complaints(complaints_id):
    """
    Logic to get complaints data
    
    Parameter:
    complaints_id (int): Id of the complaints-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Complaints.read(complaints_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@complaints_bp.route('/', methods=['POST'])
@jwt_required()
def create_complaints():
    """
    Logic to create complaints data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Complaints.create(customer_id=request.values.get('customer_id'),
		order_id=request.values.get('order_id'),
		product_id=request.values.get('product_id'),
		description=request.values.get('description'),
		resolved=request.values.get('resolved'),
		created_at=request.values.get('created_at'),
		resolved_at=request.values.get('resolved_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@complaints_bp.route('/<int:complaints_id>', methods=['PUT'])
@jwt_required()
def update_complaints(complaints_id):
    """
    Logic to update complaints data
    
    Parameter:
        complaints_id (int): Id of the complaints-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Complaints.update(complaints_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@complaints_bp.route('/<int:complaints_id>', methods=['DELETE'])
@jwt_required()
def delete_complaints(complaints_id):
    """
    Logic to delete complaints data
    
    Parameter:
        complaints_id (int): Id of the complaints-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Complaints.delete(complaints_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
