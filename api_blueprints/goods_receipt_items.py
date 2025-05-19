
from flask import Blueprint, jsonify, request
from db import Goods_receipt_items

non_id_columns = ['receipt_id', 'ingredient_id', 'qty', 'unit_price', 'tax_code_id']

goods_receipt_items_bp = Blueprint('goods_receipt_items', __name__, url_prefix='/goods_receipt_items')

@goods_receipt_items_bp.route('/<int:id>', methods=['GET'])
def get_goods_receipt_items(id):
    # Logic to get goods_receipt_items data
    result = Goods_receipt_items.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@goods_receipt_items_bp.route('/', methods=['POST'])
def create_goods_receipt_items():
    # Logic to create goods_receipt_items data
    result = Goods_receipt_items.create(receipt_id=request.values.get('receipt_id'), ingredient_id=request.values.get('ingredient_id'), qty=request.values.get('qty'), unit_price=request.values.get('unit_price'), tax_code_id=request.values.get('tax_code_id'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@goods_receipt_items_bp.route('/<int:id>', methods=['PUT'])
def update_goods_receipt_items(id):
    # Logic to update goods_receipt_items data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Goods_receipt_items.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@goods_receipt_items_bp.route('/<int:id>', methods=['DELETE'])
def delete_goods_receipt_items(id):
    # Logic to delete goods_receipt_items data
    result = Goods_receipt_items.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
