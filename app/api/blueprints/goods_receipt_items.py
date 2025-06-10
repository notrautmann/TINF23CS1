
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Goods_receipt_items

non_id_columns = ['receipt_id', 'ingredient_id', 'qty', 'unit_price', 'tax_code_id']

goods_receipt_items_bp = Blueprint('goods_receipt_items', __name__, url_prefix='/goods_receipt_items')

@goods_receipt_items_bp.route('/<int:goods_receipt_items_id>', methods=['GET'])
@jwt_required()
def get_goods_receipt_items(goods_receipt_items_id):
    # Logic to get goods_receipt_items data
    result = Goods_receipt_items.read(goods_receipt_items_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@goods_receipt_items_bp.route('/', methods=['POST'])
@jwt_required()
def create_goods_receipt_items():
    # Logic to create goods_receipt_items data
    result = Goods_receipt_items.create(receipt_id=request.values.get('receipt_id'), ingredient_id=request.values.get('ingredient_id'), qty=request.values.get('qty'), unit_price=request.values.get('unit_price'), tax_code_id=request.values.get('tax_code_id'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@goods_receipt_items_bp.route('/<int:goods_receipt_items_id>', methods=['PUT'])
@jwt_required()
def update_goods_receipt_items(goods_receipt_items_id):
    # Logic to update goods_receipt_items data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Goods_receipt_items.update(goods_receipt_items_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@goods_receipt_items_bp.route('/<int:goods_receipt_items_id>', methods=['DELETE'])
@jwt_required()
def delete_goods_receipt_items(goods_receipt_items_id):
    # Logic to delete goods_receipt_items data
    result = Goods_receipt_items.delete(goods_receipt_items_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
