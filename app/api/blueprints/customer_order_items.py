
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Customer_order_items

non_id_columns = ['order_id', 'product_id', 'quantity', 'unit_price', 'tax_code_id']

customer_order_items_bp = Blueprint('customer_order_items', __name__, url_prefix='/customer_order_items')

@customer_order_items_bp.route('/<int:customer_order_items_id>', methods=['GET'])
@jwt_required()
def get_customer_order_items(customer_order_items_id):
    # Logic to get customer_order_items data
    result = Customer_order_items.read(customer_order_items_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@customer_order_items_bp.route('/', methods=['POST'])
@jwt_required()
def create_customer_order_items():
    # Logic to create customer_order_items data
    result = Customer_order_items.create(order_id=request.values.get('order_id'), product_id=request.values.get('product_id'), quantity=request.values.get('quantity'), unit_price=request.values.get('unit_price'), tax_code_id=request.values.get('tax_code_id'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_order_items_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_customer_order_items(id):
    # Logic to update customer_order_items data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Customer_order_items.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_order_items_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_customer_order_items(id):
    # Logic to delete customer_order_items data
    result = Customer_order_items.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
