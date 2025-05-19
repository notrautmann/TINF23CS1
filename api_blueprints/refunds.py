
from flask import Blueprint, jsonify, request
from db import Refunds

non_id_columns = ['receipt_id', 'order_id', 'refund_datetime', 'total_refund_amount', 'payment_method_id', 'account_id', 'reason_id', 'created_by', 'note', 'created_at']

refunds_bp = Blueprint('refunds', __name__, url_prefix='/refunds')

@refunds_bp.route('/<int:id>', methods=['GET'])
def get_refunds(id):
    # Logic to get refunds data
    result = Refunds.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@refunds_bp.route('/', methods=['POST'])
def create_refunds():
    # Logic to create refunds data
    result = Refunds.create(receipt_id=request.values.get('receipt_id'), order_id=request.values.get('order_id'), refund_datetime=request.values.get('refund_datetime'), total_refund_amount=request.values.get('total_refund_amount'), payment_method_id=request.values.get('payment_method_id'), account_id=request.values.get('account_id'), reason_id=request.values.get('reason_id'), created_by=request.values.get('created_by'), note=request.values.get('note'), created_at=request.values.get('created_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@refunds_bp.route('/<int:id>', methods=['PUT'])
def update_refunds(id):
    # Logic to update refunds data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Refunds.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@refunds_bp.route('/<int:id>', methods=['DELETE'])
def delete_refunds(id):
    # Logic to delete refunds data
    result = Refunds.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
