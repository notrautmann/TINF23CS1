
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Product_allergens

non_id_columns = ['product_id',
	'allergen_id']

product_allergens_bp = Blueprint('product_allergens',
    __name__,
    url_prefix='/product_allergens')

@product_allergens_bp.route('/<int:product_allergens_id>', methods=['GET'])
@jwt_required()
def get_product_allergens(product_allergens_id):
    # Logic to get product_allergens data
    result = Product_allergens.read(product_allergens_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@product_allergens_bp.route('/', methods=['POST'])
@jwt_required()
def create_product_allergens():
    # Logic to create product_allergens data
    result = Product_allergens.create(product_id=request.values.get('product_id'),
		allergen_id=request.values.get('allergen_id'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@product_allergens_bp.route('/<int:product_allergens_id>', methods=['PUT'])
@jwt_required()
def update_product_allergens(product_allergens_id):
    # Logic to update product_allergens data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Product_allergens.update(product_allergens_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@product_allergens_bp.route('/<int:product_allergens_id>', methods=['DELETE'])
@jwt_required()
def delete_product_allergens(product_allergens_id):
    # Logic to delete product_allergens data
    result = Product_allergens.delete(product_allergens_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
