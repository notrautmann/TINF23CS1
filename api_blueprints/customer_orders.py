
from flask import Blueprint, jsonify, request
from db import Customer_orders

non_id_columns = ['order_number', 'customer_id', 'customer_name', 'branch_id', 'order_datetime', 'desired_datetime', 'serial', 'serial_end', 'status', 'total_amount', 'payment_status', 'comment']

customer_orders_bp = Blueprint('customer_orders', __name__, url_prefix='/customer_orders')

@customer_orders_bp.route('/<int:id>', methods=['GET'])
def get_customer_orders(id):
    # Logic to get customer_orders data
    result = Customer_orders.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@customer_orders_bp.route('/', methods=['POST'])
def create_customer_orders():
    # Logic to create customer_orders data
    result = Customer_orders.create(order_number=request.values.get('order_number'), customer_id=request.values.get('customer_id'), customer_name=request.values.get('customer_name'), branch_id=request.values.get('branch_id'), order_datetime=request.values.get('order_datetime'), desired_datetime=request.values.get('desired_datetime'), serial=request.values.get('serial'), serial_end=request.values.get('serial_end'), status=request.values.get('status'), total_amount=request.values.get('total_amount'), payment_status=request.values.get('payment_status'), comment=request.values.get('comment'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_orders_bp.route('/<int:id>', methods=['PUT'])
def update_customer_orders(id):
    # Logic to update customer_orders data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Customer_orders.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@customer_orders_bp.route('/<int:id>', methods=['DELETE'])
def delete_customer_orders(id):
    # Logic to delete customer_orders data
    result = Customer_orders.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
