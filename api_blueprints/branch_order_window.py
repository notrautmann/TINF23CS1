
from flask import Blueprint, jsonify, request
from db import Branch_order_window

branch_order_window_bp = Blueprint('branch_order_window', __name__, url_prefix='/branch_order_window')

@branch_order_window_bp.route('/<int:id>', methods=['GET'])
def get_branch_order_window(id):
    # Logic to get branch_order_window data
    result = Branch_order_window.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@branch_order_window_bp.route('/', methods=['POST'])
def create_branch_order_window():
    # Logic to create branch_order_window data
    result = Branch_order_window.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@branch_order_window_bp.route('/<int:id>', methods=['PUT'])
def update_branch_order_window(id):
    # Logic to update branch_order_window data
    result = Branch_order_window.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@branch_order_window_bp.route('/<int:id>', methods=['DELETE'])
def delete_branch_order_window(id):
    # Logic to delete branch_order_window data
    result = Branch_order_window.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
