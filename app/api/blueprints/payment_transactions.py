"""
Implements the CRUD-operations for the payment_transactions-table.

Functions:

    get_payment_transactions(payment_transactions_id)
    create_payment_transactions()
    update_payment_transactions(payment_transactions_id)
    delete_payment_transactions(payment_transactions_id)

Misc variables:

    payment_transactions_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Payment_transactions

non_id_columns = ['account_id',
	'payment_method_id',
	'reference_type',
	'reference_id',
	'amount',
	'currency',
	'direction',
	'transaction_date',
	'created_at']

payment_transactions_bp = Blueprint('payment_transactions',
    __name__,
    url_prefix='/payment_transactions')

@payment_transactions_bp.route('/<int:payment_transactions_id>', methods=['GET'])
@jwt_required()
def get_payment_transactions(payment_transactions_id):
    """
    Logic to get payment_transactions data
    
    Parameter:
    payment_transactions_id (int): Id of the payment_transactions-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Payment_transactions.read(payment_transactions_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@payment_transactions_bp.route('/', methods=['POST'])
@jwt_required()
def create_payment_transactions():
    """
    Logic to create payment_transactions data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Payment_transactions.create(account_id=request.values.get('account_id'),
		payment_method_id=request.values.get('payment_method_id'),
		reference_type=request.values.get('reference_type'),
		reference_id=request.values.get('reference_id'),
		amount=request.values.get('amount'),
		currency=request.values.get('currency'),
		direction=request.values.get('direction'),
		transaction_date=request.values.get('transaction_date'),
		created_at=request.values.get('created_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@payment_transactions_bp.route('/<int:payment_transactions_id>', methods=['PUT'])
@jwt_required()
def update_payment_transactions(payment_transactions_id):
    """
    Logic to update payment_transactions data
    
    Parameter:
        payment_transactions_id (int): Id of the payment_transactions-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Payment_transactions.update(payment_transactions_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@payment_transactions_bp.route('/<int:payment_transactions_id>', methods=['DELETE'])
@jwt_required()
def delete_payment_transactions(payment_transactions_id):
    """
    Logic to delete payment_transactions data
    
    Parameter:
        payment_transactions_id (int): Id of the payment_transactions-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Payment_transactions.delete(payment_transactions_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
