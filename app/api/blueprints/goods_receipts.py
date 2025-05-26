
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Goods_receipts

non_id_columns = ['receipt_number', 'supplier_order_id', 'receipt_date', 'created_at']

goods_receipts_bp = Blueprint('goods_receipts', __name__, url_prefix='/goods_receipts')

@goods_receipts_bp.route('/<int:goods_receipts_id>', methods=['GET'])
@jwt_required()
def get_goods_receipts(goods_receipts_id):
    # Logic to get goods_receipts data
    result = Goods_receipts.read(goods_receipts_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@goods_receipts_bp.route('/', methods=['POST'])
@jwt_required()
def create_goods_receipts():
    # Logic to create goods_receipts data
    result = Goods_receipts.create(receipt_number=request.values.get('receipt_number'), supplier_order_id=request.values.get('supplier_order_id'), receipt_date=request.values.get('receipt_date'), created_at=request.values.get('created_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@goods_receipts_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_goods_receipts(id):
    # Logic to update goods_receipts data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Goods_receipts.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@goods_receipts_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_goods_receipts(id):
    # Logic to delete goods_receipts data
    result = Goods_receipts.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
