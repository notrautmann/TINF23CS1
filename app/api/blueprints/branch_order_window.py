
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Branch_order_window

non_id_columns = ['branch_id',
	'weekday',
	'order_start',
	'order_end']

branch_order_window_bp = Blueprint('branch_order_window',
    __name__,
    url_prefix='/branch_order_window')

@branch_order_window_bp.route('/<int:branch_order_window_id>', methods=['GET'])
@jwt_required()
def get_branch_order_window(branch_order_window_id):
    # Logic to get branch_order_window data
    result = Branch_order_window.read(branch_order_window_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@branch_order_window_bp.route('/', methods=['POST'])
@jwt_required()
def create_branch_order_window():
    # Logic to create branch_order_window data
    result = Branch_order_window.create(branch_id=request.values.get('branch_id'),
		weekday=request.values.get('weekday'),
		order_start=request.values.get('order_start'),
		order_end=request.values.get('order_end'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@branch_order_window_bp.route('/<int:branch_order_window_id>', methods=['PUT'])
@jwt_required()
def update_branch_order_window(branch_order_window_id):
    # Logic to update branch_order_window data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Branch_order_window.update(branch_order_window_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@branch_order_window_bp.route('/<int:branch_order_window_id>', methods=['DELETE'])
@jwt_required()
def delete_branch_order_window(branch_order_window_id):
    # Logic to delete branch_order_window data
    result = Branch_order_window.delete(branch_order_window_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
