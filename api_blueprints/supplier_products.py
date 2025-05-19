
from flask import Blueprint, jsonify, request
from db import Supplier_products

non_id_columns = ['supplier_id', 'ingredient_id', 'supplier_sku', 'purchase_price', 'min_order_qty', 'lead_time_days']

supplier_products_bp = Blueprint('supplier_products', __name__, url_prefix='/supplier_products')

@supplier_products_bp.route('/<int:id>', methods=['GET'])
def get_supplier_products(id):
    # Logic to get supplier_products data
    result = Supplier_products.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@supplier_products_bp.route('/', methods=['POST'])
def create_supplier_products():
    # Logic to create supplier_products data
    result = Supplier_products.create(supplier_id=request.values.get('supplier_id'), ingredient_id=request.values.get('ingredient_id'), supplier_sku=request.values.get('supplier_sku'), purchase_price=request.values.get('purchase_price'), min_order_qty=request.values.get('min_order_qty'), lead_time_days=request.values.get('lead_time_days'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_products_bp.route('/<int:id>', methods=['PUT'])
def update_supplier_products(id):
    # Logic to update supplier_products data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Supplier_products.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_products_bp.route('/<int:id>', methods=['DELETE'])
def delete_supplier_products(id):
    # Logic to delete supplier_products data
    result = Supplier_products.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
