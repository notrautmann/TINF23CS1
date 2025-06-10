"""
Implements the CRUD-operations for the payment_methods-table.

Functions:

    get_payment_methods(payment_methods_id)
    create_payment_methods()
    update_payment_methods(payment_methods_id)
    delete_payment_methods(payment_methods_id)

Misc variables:

    payment_methods_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Payment_methods

non_id_columns = ['name',
	'external_code',
	'is_cash']

payment_methods_bp = Blueprint('payment_methods',
    __name__,
    url_prefix='/payment_methods')

@payment_methods_bp.route('/<int:payment_methods_id>', methods=['GET'])
@jwt_required()
def get_payment_methods(payment_methods_id):
    """
    Logic to get payment_methods data
    
    Parameter:
    payment_methods_id (int): Id of the payment_methods-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Payment_methods.read(payment_methods_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@payment_methods_bp.route('/', methods=['POST'])
@jwt_required()
def create_payment_methods():
    """
    Logic to create payment_methods data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Payment_methods.create(name=request.values.get('name'),
		external_code=request.values.get('external_code'),
		is_cash=request.values.get('is_cash'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@payment_methods_bp.route('/<int:payment_methods_id>', methods=['PUT'])
@jwt_required()
def update_payment_methods(payment_methods_id):
    """
    Logic to update payment_methods data
    
    Parameter:
        payment_methods_id (int): Id of the payment_methods-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Payment_methods.update(payment_methods_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@payment_methods_bp.route('/<int:payment_methods_id>', methods=['DELETE'])
@jwt_required()
def delete_payment_methods(payment_methods_id):
    """
    Logic to delete payment_methods data
    
    Parameter:
        payment_methods_id (int): Id of the payment_methods-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Payment_methods.delete(payment_methods_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
