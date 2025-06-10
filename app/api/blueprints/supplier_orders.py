"""
Implements the CRUD-operations for the supplier_orders-table.

Functions:

    get_supplier_orders(supplier_orders_id)
    create_supplier_orders()
    update_supplier_orders(supplier_orders_id)
    delete_supplier_orders(supplier_orders_id)

Misc variables:

    supplier_orders_id    
"""
    
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Supplier_orders

non_id_columns = ['order_number',
	'supplier_id',
	'branch_id',
	'order_date',
	'status',
	'expected_date',
	'total_amount']

supplier_orders_bp = Blueprint('supplier_orders',
    __name__,
    url_prefix='/supplier_orders')

@supplier_orders_bp.route('/<int:supplier_orders_id>', methods=['GET'])
@jwt_required()
def get_supplier_orders(supplier_orders_id):
    """
    Logic to get supplier_orders data
    
    Parameter:
    supplier_orders_id (int): Id of the supplier_orders-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Supplier_orders.read(supplier_orders_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@supplier_orders_bp.route('/', methods=['POST'])
@jwt_required()
def create_supplier_orders():
    """
    Logic to create supplier_orders data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Supplier_orders.create(order_number=request.values.get('order_number'),
		supplier_id=request.values.get('supplier_id'),
		branch_id=request.values.get('branch_id'),
		order_date=request.values.get('order_date'),
		status=request.values.get('status'),
		expected_date=request.values.get('expected_date'),
		total_amount=request.values.get('total_amount'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@supplier_orders_bp.route('/<int:supplier_orders_id>', methods=['PUT'])
@jwt_required()
def update_supplier_orders(supplier_orders_id):
    """
    Logic to update supplier_orders data
    
    Parameter:
        supplier_orders_id (int): Id of the supplier_orders-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Supplier_orders.update(supplier_orders_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@supplier_orders_bp.route('/<int:supplier_orders_id>', methods=['DELETE'])
@jwt_required()
def delete_supplier_orders(supplier_orders_id):
    """
    Logic to delete supplier_orders data
    
    Parameter:
        supplier_orders_id (int): Id of the supplier_orders-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Supplier_orders.delete(supplier_orders_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
