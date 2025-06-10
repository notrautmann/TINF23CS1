"""
Implements the CRUD-operations for the sales_receipt_items-table.

Functions:

    get_sales_receipt_items(sales_receipt_items_id)
    create_sales_receipt_items()
    update_sales_receipt_items(sales_receipt_items_id)
    delete_sales_receipt_items(sales_receipt_items_id)

Misc variables:

    sales_receipt_items_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.records.sales_receipt_items import Sales_receipt_items

non_id_columns = ['receipt_id',
	'product_id',
	'qty',
	'unit_price',
	'tax_code_id']

sales_receipt_items_bp = Blueprint('sales_receipt_items',
    __name__,
    url_prefix='/sales_receipt_items')

@sales_receipt_items_bp.route('/<int:sales_receipt_items_id>', methods=['GET'])
@jwt_required()
def get_sales_receipt_items(sales_receipt_items_id):
    """
    Logic to get sales_receipt_items data
    
    Parameter:
    sales_receipt_items_id (int): Id of the sales_receipt_items-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Sales_receipt_items.read(sales_receipt_items_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@sales_receipt_items_bp.route('/', methods=['POST'])
@jwt_required()
def create_sales_receipt_items():
    """
    Logic to create sales_receipt_items data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Sales_receipt_items.create(receipt_id=request.values.get('receipt_id'),
		product_id=request.values.get('product_id'),
		qty=request.values.get('qty'),
		unit_price=request.values.get('unit_price'),
		tax_code_id=request.values.get('tax_code_id'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@sales_receipt_items_bp.route('/<int:sales_receipt_items_id>', methods=['PUT'])
@jwt_required()
def update_sales_receipt_items(sales_receipt_items_id):
    """
    Logic to update sales_receipt_items data
    
    Parameter:
        sales_receipt_items_id (int): Id of the sales_receipt_items-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Sales_receipt_items.update(sales_receipt_items_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@sales_receipt_items_bp.route('/<int:sales_receipt_items_id>', methods=['DELETE'])
@jwt_required()
def delete_sales_receipt_items(sales_receipt_items_id):
    """
    Logic to delete sales_receipt_items data
    
    Parameter:
        sales_receipt_items_id (int): Id of the sales_receipt_items-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Sales_receipt_items.delete(sales_receipt_items_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
