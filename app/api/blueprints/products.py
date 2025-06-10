"""
Implements the CRUD-operations for the products-table.

Functions:

    get_products(products_id)
    create_products()
    update_products(products_id)
    delete_products(products_id)

Misc variables:

    products_id    
"""
    
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Products

non_id_columns = ['name',
	'sku',
	'recipe_id',
	'sales_price',
	'tax_code_id',
	'is_active',
	'created_at',
	'updated_at']

products_bp = Blueprint('products',
    __name__,
    url_prefix='/products')

@products_bp.route('/<int:products_id>', methods=['GET'])
@jwt_required()
def get_products(products_id):
    """
    Logic to get products data
    
    Parameter:
    products_id (int): Id of the products-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Products.read(products_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@products_bp.route('/', methods=['POST'])
@jwt_required()
def create_products():
    """
    Logic to create products data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Products.create(name=request.values.get('name'),
		sku=request.values.get('sku'),
		recipe_id=request.values.get('recipe_id'),
		sales_price=request.values.get('sales_price'),
		tax_code_id=request.values.get('tax_code_id'),
		is_active=request.values.get('is_active'),
		created_at=request.values.get('created_at'),
		updated_at=request.values.get('updated_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@products_bp.route('/<int:products_id>', methods=['PUT'])
@jwt_required()
def update_products(products_id):
    """
    Logic to update products data
    
    Parameter:
        products_id (int): Id of the products-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Products.update(products_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@products_bp.route('/<int:products_id>', methods=['DELETE'])
@jwt_required()
def delete_products(products_id):
    """
    Logic to delete products data
    
    Parameter:
        products_id (int): Id of the products-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    """
    result = Products.delete(products_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
