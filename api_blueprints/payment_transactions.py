
from flask import Blueprint, jsonify, request
from db import Payment_transactions

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
    result = Payment_transactions.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@payment_transactions_bp.route('/<int:id>', methods=['PUT'])
def update_payment_transactions(id):
    # Logic to update payment_transactions data
    result = Payment_transactions.update(request.values())
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
