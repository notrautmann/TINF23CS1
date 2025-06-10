"""
Implements the CRUD-operations for the sales_receipts-table.

Functions:

    get_sales_receipts(sales_receipts_id)
    create_sales_receipts()
    update_sales_receipts(sales_receipts_id)
    delete_sales_receipts(sales_receipts_id)

Misc variables:

    sales_receipts_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Sales_receipts

non_id_columns = ['receipt_number',
	'branch_id',
	'pos_terminal_id',
	'sale_datetime',
	'customer_id',
	'total_amount',
	'payment_method_id',
	'payment_reference']

sales_receipts_bp = Blueprint('sales_receipts',
    __name__,
    url_prefix='/sales_receipts')

@sales_receipts_bp.route('/<int:sales_receipts_id>', methods=['GET'])
@jwt_required()
def get_sales_receipts(sales_receipts_id):
    """
    Logic to get sales_receipts data
    
    Parameter:
    sales_receipts_id (int): Id of the sales_receipts-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Sales_receipts.read(sales_receipts_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@sales_receipts_bp.route('/', methods=['POST'])
@jwt_required()
def create_sales_receipts():
    """
    Logic to create sales_receipts data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Sales_receipts.create(receipt_number=request.values.get('receipt_number'),
		branch_id=request.values.get('branch_id'),
		pos_terminal_id=request.values.get('pos_terminal_id'),
		sale_datetime=request.values.get('sale_datetime'),
		customer_id=request.values.get('customer_id'),
		total_amount=request.values.get('total_amount'),
		payment_method_id=request.values.get('payment_method_id'),
		payment_reference=request.values.get('payment_reference'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@sales_receipts_bp.route('/<int:sales_receipts_id>', methods=['PUT'])
@jwt_required()
def update_sales_receipts(sales_receipts_id):
    """
    Logic to update sales_receipts data
    
    Parameter:
        sales_receipts_id (int): Id of the sales_receipts-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Sales_receipts.update(sales_receipts_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@sales_receipts_bp.route('/<int:sales_receipts_id>', methods=['DELETE'])
@jwt_required()
def delete_sales_receipts(sales_receipts_id):
    """
    Logic to delete sales_receipts data
    
    Parameter:
        sales_receipts_id (int): Id of the sales_receipts-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Sales_receipts.delete(sales_receipts_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
