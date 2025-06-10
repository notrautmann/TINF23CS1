"""
Implements the CRUD-operations for the goods_receipts-table.

Functions:

    get_goods_receipts(goods_receipts_id)
    create_goods_receipts()
    update_goods_receipts(goods_receipts_id)
    delete_goods_receipts(goods_receipts_id)

Misc variables:

    goods_receipts_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.records.goods_receipts import Goods_receipts

non_id_columns = ['receipt_number',
	'supplier_order_id',
	'receipt_date',
	'created_at']

goods_receipts_bp = Blueprint('goods_receipts',
    __name__,
    url_prefix='/goods_receipts')

@goods_receipts_bp.route('/<int:goods_receipts_id>', methods=['GET'])
@jwt_required()
def get_goods_receipts(goods_receipts_id):
    """
    Logic to get goods_receipts data
    
    Parameter:
    goods_receipts_id (int): Id of the goods_receipts-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Goods_receipts.read(goods_receipts_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@goods_receipts_bp.route('/', methods=['POST'])
@jwt_required()
def create_goods_receipts():
    """
    Logic to create goods_receipts data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Goods_receipts.create(receipt_number=request.values.get('receipt_number'),
		supplier_order_id=request.values.get('supplier_order_id'),
		receipt_date=request.values.get('receipt_date'),
		created_at=request.values.get('created_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@goods_receipts_bp.route('/<int:goods_receipts_id>', methods=['PUT'])
@jwt_required()
def update_goods_receipts(goods_receipts_id):
    """
    Logic to update goods_receipts data
    
    Parameter:
        goods_receipts_id (int): Id of the goods_receipts-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Goods_receipts.update(goods_receipts_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@goods_receipts_bp.route('/<int:goods_receipts_id>', methods=['DELETE'])
@jwt_required()
def delete_goods_receipts(goods_receipts_id):
    """
    Logic to delete goods_receipts data
    
    Parameter:
        goods_receipts_id (int): Id of the goods_receipts-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Goods_receipts.delete(goods_receipts_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
