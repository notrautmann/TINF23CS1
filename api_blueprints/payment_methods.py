
from flask import Blueprint, jsonify, request
from db import Payment_methods

payment_methods_bp = Blueprint('payment_methods', __name__, url_prefix='/payment_methods')

@payment_methods_bp.route('/<int:id>', methods=['GET'])
def get_payment_methods(id):
    # Logic to get payment_methods data
    result = Payment_methods.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@payment_methods_bp.route('/', methods=['POST'])
def create_payment_methods():
    # Logic to create payment_methods data
    result = Payment_methods.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@payment_methods_bp.route('/<int:id>', methods=['PUT'])
def update_payment_methods(id):
    # Logic to update payment_methods data
    result = Payment_methods.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@payment_methods_bp.route('/<int:id>', methods=['DELETE'])
def delete_payment_methods(id):
    # Logic to delete payment_methods data
    result = Payment_methods.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
