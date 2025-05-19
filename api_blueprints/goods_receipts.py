
from flask import Blueprint, jsonify, request
from db import Goods_receipts

goods_receipts_bp = Blueprint('goods_receipts', __name__, url_prefix='/goods_receipts')

@goods_receipts_bp.route('/<int:id>', methods=['GET'])
def get_goods_receipts(id):
    # Logic to get goods_receipts data
    result = Goods_receipts.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@goods_receipts_bp.route('/', methods=['POST'])
def create_goods_receipts():
    # Logic to create goods_receipts data
    result = Goods_receipts.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@goods_receipts_bp.route('/<int:id>', methods=['PUT'])
def update_goods_receipts(id):
    # Logic to update goods_receipts data
    result = Goods_receipts.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@goods_receipts_bp.route('/<int:id>', methods=['DELETE'])
def delete_goods_receipts(id):
    # Logic to delete goods_receipts data
    result = Goods_receipts.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
