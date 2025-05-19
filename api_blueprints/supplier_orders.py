
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from db import Supplier_orders

non_id_columns = ['order_number', 'supplier_id', 'branch_id', 'order_date', 'status', 'expected_date', 'total_amount']

supplier_orders_bp = Blueprint('supplier_orders', __name__, url_prefix='/supplier_orders')

@supplier_orders_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_supplier_orders(id):
    # Logic to get supplier_orders data
    result = Supplier_orders.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@supplier_orders_bp.route('/', methods=['POST'])
@jwt_required()
def create_supplier_orders():
    # Logic to create supplier_orders data
    result = Supplier_orders.create(order_number=request.values.get('order_number'), supplier_id=request.values.get('supplier_id'), branch_id=request.values.get('branch_id'), order_date=request.values.get('order_date'), status=request.values.get('status'), expected_date=request.values.get('expected_date'), total_amount=request.values.get('total_amount'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_orders_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_supplier_orders(id):
    # Logic to update supplier_orders data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Supplier_orders.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_orders_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_supplier_orders(id):
    # Logic to delete supplier_orders data
    result = Supplier_orders.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
