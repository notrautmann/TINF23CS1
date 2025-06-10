"""
Implements the CRUD-operations for the customer_orders-table.

Functions:

    get_customer_orders(customer_orders_id)
    create_customer_orders()
    update_customer_orders(customer_orders_id)
    delete_customer_orders(customer_orders_id)

Misc variables:

    customer_orders_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Customer_orders

non_id_columns = ['order_number',
	'customer_id',
	'customer_name',
	'branch_id',
	'order_datetime',
	'desired_datetime',
	'serial',
	'serial_end',
	'status',
	'total_amount',
	'payment_status',
	'comment']

customer_orders_bp = Blueprint('customer_orders',
    __name__,
    url_prefix='/customer_orders')

@customer_orders_bp.route('/<int:customer_orders_id>', methods=['GET'])
@jwt_required()
def get_customer_orders(customer_orders_id):
    """
    Logic to get customer_orders data
    
    Parameter:
    customer_orders_id (int): Id of the customer_orders-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Customer_orders.read(customer_orders_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@customer_orders_bp.route('/', methods=['POST'])
@jwt_required()
def create_customer_orders():
    """
    Logic to create customer_orders data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Customer_orders.create(order_number=request.values.get('order_number'),
		customer_id=request.values.get('customer_id'),
		customer_name=request.values.get('customer_name'),
		branch_id=request.values.get('branch_id'),
		order_datetime=request.values.get('order_datetime'),
		desired_datetime=request.values.get('desired_datetime'),
		serial=request.values.get('serial'),
		serial_end=request.values.get('serial_end'),
		status=request.values.get('status'),
		total_amount=request.values.get('total_amount'),
		payment_status=request.values.get('payment_status'),
		comment=request.values.get('comment'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@customer_orders_bp.route('/<int:customer_orders_id>', methods=['PUT'])
@jwt_required()
def update_customer_orders(customer_orders_id):
    """
    Logic to update customer_orders data
    
    Parameter:
        customer_orders_id (int): Id of the customer_orders-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Customer_orders.update(customer_orders_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@customer_orders_bp.route('/<int:customer_orders_id>', methods=['DELETE'])
@jwt_required()
def delete_customer_orders(customer_orders_id):
    """
    Logic to delete customer_orders data
    
    Parameter:
        customer_orders_id (int): Id of the customer_orders-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Customer_orders.delete(customer_orders_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
