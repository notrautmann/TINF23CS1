
from flask import Blueprint, jsonify, request
from db import Sales_receipts

sales_receipts_bp = Blueprint('sales_receipts', __name__, url_prefix='/sales_receipts')

@sales_receipts_bp.route('/<int:id>', methods=['GET'])
def get_sales_receipts(id):
    # Logic to get sales_receipts data
    result = Sales_receipts.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@sales_receipts_bp.route('/', methods=['POST'])
def create_sales_receipts():
    # Logic to create sales_receipts data
    result = Sales_receipts.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@sales_receipts_bp.route('/<int:id>', methods=['PUT'])
def update_sales_receipts(id):
    # Logic to update sales_receipts data
    result = Sales_receipts.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@sales_receipts_bp.route('/<int:id>', methods=['DELETE'])
def delete_sales_receipts(id):
    # Logic to delete sales_receipts data
    result = Sales_receipts.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
