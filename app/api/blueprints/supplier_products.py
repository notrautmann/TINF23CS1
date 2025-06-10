"""
Implements the CRUD-operations for the supplier_products-table.

Functions:

    get_supplier_products(supplier_products_id)
    create_supplier_products()
    update_supplier_products(supplier_products_id)
    delete_supplier_products(supplier_products_id)

Misc variables:

    supplier_products_id    
"""
    
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Supplier_products

non_id_columns = ['supplier_id',
	'ingredient_id',
	'supplier_sku',
	'purchase_price',
	'min_order_qty',
	'lead_time_days']

supplier_products_bp = Blueprint('supplier_products',
    __name__,
    url_prefix='/supplier_products')

@supplier_products_bp.route('/<int:supplier_products_id>', methods=['GET'])
@jwt_required()
def get_supplier_products(supplier_products_id):
    """
    Logic to get supplier_products data
    
    Parameter:
    supplier_products_id (int): Id of the supplier_products-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Supplier_products.read(supplier_products_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@supplier_products_bp.route('/', methods=['POST'])
@jwt_required()
def create_supplier_products():
    """
    Logic to create supplier_products data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Supplier_products.create(supplier_id=request.values.get('supplier_id'),
		ingredient_id=request.values.get('ingredient_id'),
		supplier_sku=request.values.get('supplier_sku'),
		purchase_price=request.values.get('purchase_price'),
		min_order_qty=request.values.get('min_order_qty'),
		lead_time_days=request.values.get('lead_time_days'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@supplier_products_bp.route('/<int:supplier_products_id>', methods=['PUT'])
@jwt_required()
def update_supplier_products(supplier_products_id):
    """
    Logic to update supplier_products data
    
    Parameter:
        supplier_products_id (int): Id of the supplier_products-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Supplier_products.update(supplier_products_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@supplier_products_bp.route('/<int:supplier_products_id>', methods=['DELETE'])
@jwt_required()
def delete_supplier_products(supplier_products_id):
    """
    Logic to delete supplier_products data
    
    Parameter:
        supplier_products_id (int): Id of the supplier_products-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Supplier_products.delete(supplier_products_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
