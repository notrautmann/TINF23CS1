
from flask import Blueprint, jsonify, request
from db import Sales_receipt_items

non_id_columns = ['receipt_id', 'product_id', 'qty', 'unit_price', 'tax_code_id']

sales_receipt_items_bp = Blueprint('sales_receipt_items', __name__, url_prefix='/sales_receipt_items')

@sales_receipt_items_bp.route('/<int:id>', methods=['GET'])
def get_sales_receipt_items(id):
    # Logic to get sales_receipt_items data
    result = Sales_receipt_items.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@sales_receipt_items_bp.route('/', methods=['POST'])
def create_sales_receipt_items():
    # Logic to create sales_receipt_items data
    result = Sales_receipt_items.create(receipt_id=request.values.get('receipt_id'), product_id=request.values.get('product_id'), qty=request.values.get('qty'), unit_price=request.values.get('unit_price'), tax_code_id=request.values.get('tax_code_id'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@sales_receipt_items_bp.route('/<int:id>', methods=['PUT'])
def update_sales_receipt_items(id):
    # Logic to update sales_receipt_items data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Sales_receipt_items.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@sales_receipt_items_bp.route('/<int:id>', methods=['DELETE'])
def delete_sales_receipt_items(id):
    # Logic to delete sales_receipt_items data
    result = Sales_receipt_items.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
