
from flask import Blueprint, jsonify, request
from db import Customer_order_items

non_id_columns = ['order_id', 'product_id', 'quantity', 'unit_price', 'tax_code_id']

customer_order_items_bp = Blueprint('customer_order_items', __name__, url_prefix='/customer_order_items')

@customer_order_items_bp.route('/<int:id>', methods=['GET'])
def get_customer_order_items(id):
    # Logic to get customer_order_items data
    result = Customer_order_items.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@customer_order_items_bp.route('/', methods=['POST'])
def create_customer_order_items():
    # Logic to create customer_order_items data
    result = Customer_order_items.create(order_id=request.values.get('order_id'), product_id=request.values.get('product_id'), quantity=request.values.get('quantity'), unit_price=request.values.get('unit_price'), tax_code_id=request.values.get('tax_code_id'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_order_items_bp.route('/<int:id>', methods=['PUT'])
def update_customer_order_items(id):
    # Logic to update customer_order_items data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Customer_order_items.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_order_items_bp.route('/<int:id>', methods=['DELETE'])
def delete_customer_order_items(id):
    # Logic to delete customer_order_items data
    result = Customer_order_items.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
