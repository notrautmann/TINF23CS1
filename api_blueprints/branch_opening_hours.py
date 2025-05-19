
from flask import Blueprint, jsonify, request
from db import Branch_opening_hours

branch_opening_hours_bp = Blueprint('branch_opening_hours', __name__, url_prefix='/branch_opening_hours')

@branch_opening_hours_bp.route('/<int:id>', methods=['GET'])
def get_branch_opening_hours(id):
    # Logic to get branch_opening_hours data
    result = Branch_opening_hours.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@branch_opening_hours_bp.route('/', methods=['POST'])
def create_branch_opening_hours():
    # Logic to create branch_opening_hours data
    result = Branch_opening_hours.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@branch_opening_hours_bp.route('/<int:id>', methods=['PUT'])
def update_branch_opening_hours(id):
    # Logic to update branch_opening_hours data
    result = Branch_opening_hours.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@branch_opening_hours_bp.route('/<int:id>', methods=['DELETE'])
def delete_branch_opening_hours(id):
    # Logic to delete branch_opening_hours data
    result = Branch_opening_hours.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
