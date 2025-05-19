
from flask import Blueprint, jsonify, request
from db import Payment_transactions

non_id_columns = ['account_id', 'payment_method_id', 'reference_type', 'reference_id', 'amount', 'currency', 'direction', 'transaction_date', 'created_at']

payment_transactions_bp = Blueprint('payment_transactions', __name__, url_prefix='/payment_transactions')

@payment_transactions_bp.route('/<int:id>', methods=['GET'])
def get_payment_transactions(id):
    # Logic to get payment_transactions data
    result = Payment_transactions.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@payment_transactions_bp.route('/', methods=['POST'])
def create_payment_transactions():
    # Logic to create payment_transactions data
    result = Payment_transactions.create(account_id=request.values.get('account_id'), payment_method_id=request.values.get('payment_method_id'), reference_type=request.values.get('reference_type'), reference_id=request.values.get('reference_id'), amount=request.values.get('amount'), currency=request.values.get('currency'), direction=request.values.get('direction'), transaction_date=request.values.get('transaction_date'), created_at=request.values.get('created_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@payment_transactions_bp.route('/<int:id>', methods=['PUT'])
def update_payment_transactions(id):
    # Logic to update payment_transactions data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Payment_transactions.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@payment_transactions_bp.route('/<int:id>', methods=['DELETE'])
def delete_payment_transactions(id):
    # Logic to delete payment_transactions data
    result = Payment_transactions.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
