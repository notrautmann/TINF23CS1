
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Refunds

non_id_columns = ['receipt_id', 'order_id', 'refund_datetime', 'total_refund_amount', 'payment_method_id', 'account_id', 'reason_id', 'created_by', 'note', 'created_at']

refunds_bp = Blueprint('refunds', __name__, url_prefix='/refunds')

@refunds_bp.route('/<int:refunds_id>', methods=['GET'])
@jwt_required()
def get_refunds(refunds_id):
    # Logic to get refunds data
    result = Refunds.read(refunds_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@refunds_bp.route('/', methods=['POST'])
@jwt_required()
def create_refunds():
    # Logic to create refunds data
    result = Refunds.create(receipt_id=request.values.get('receipt_id'), order_id=request.values.get('order_id'), refund_datetime=request.values.get('refund_datetime'), total_refund_amount=request.values.get('total_refund_amount'), payment_method_id=request.values.get('payment_method_id'), account_id=request.values.get('account_id'), reason_id=request.values.get('reason_id'), created_by=request.values.get('created_by'), note=request.values.get('note'), created_at=request.values.get('created_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@refunds_bp.route('/<int:refunds_id>', methods=['PUT'])
@jwt_required()
def update_refunds(refunds_id):
    # Logic to update refunds data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Refunds.update(refunds_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@refunds_bp.route('/<int:refunds_id>', methods=['DELETE'])
@jwt_required()
def delete_refunds(refunds_id):
    # Logic to delete refunds data
    result = Refunds.delete(refunds_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
