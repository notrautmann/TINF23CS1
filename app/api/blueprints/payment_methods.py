
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Payment_methods

non_id_columns = ['name', 'external_code', 'is_cash']

payment_methods_bp = Blueprint('payment_methods', __name__, url_prefix='/payment_methods')

@payment_methods_bp.route('/<int:payment_methods_id>', methods=['GET'])
@jwt_required()
def get_payment_methods(payment_methods_id):
    # Logic to get payment_methods data
    result = Payment_methods.read(payment_methods_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@payment_methods_bp.route('/', methods=['POST'])
@jwt_required()
def create_payment_methods():
    # Logic to create payment_methods data
    result = Payment_methods.create(name=request.values.get('name'), external_code=request.values.get('external_code'), is_cash=request.values.get('is_cash'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@payment_methods_bp.route('/<int:payment_methods_id>', methods=['PUT'])
@jwt_required()
def update_payment_methods(payment_methods_id):
    # Logic to update payment_methods data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Payment_methods.update(payment_methods_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@payment_methods_bp.route('/<int:payment_methods_id>', methods=['DELETE'])
@jwt_required()
def delete_payment_methods(payment_methods_id):
    # Logic to delete payment_methods data
    result = Payment_methods.delete(payment_methods_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
