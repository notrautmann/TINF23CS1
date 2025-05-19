
from flask import Blueprint, jsonify, request
from db import Refund_items

non_id_columns = ['refund_id', 'product_id', 'qty', 'unit_price', 'tax_code_id']

refund_items_bp = Blueprint('refund_items', __name__, url_prefix='/refund_items')

@refund_items_bp.route('/<int:id>', methods=['GET'])
def get_refund_items(id):
    # Logic to get refund_items data
    result = Refund_items.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@refund_items_bp.route('/', methods=['POST'])
def create_refund_items():
    # Logic to create refund_items data
    result = Refund_items.create(refund_id=request.values.get('refund_id'), product_id=request.values.get('product_id'), qty=request.values.get('qty'), unit_price=request.values.get('unit_price'), tax_code_id=request.values.get('tax_code_id'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@refund_items_bp.route('/<int:id>', methods=['PUT'])
def update_refund_items(id):
    # Logic to update refund_items data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Refund_items.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@refund_items_bp.route('/<int:id>', methods=['DELETE'])
def delete_refund_items(id):
    # Logic to delete refund_items data
    result = Refund_items.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
