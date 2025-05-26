
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Branch_opening_hours

non_id_columns = ['branch_id', 'weekday', 'opens', 'closes']

branch_opening_hours_bp = Blueprint('branch_opening_hours', __name__, url_prefix='/branch_opening_hours')

@branch_opening_hours_bp.route('/<int:branch_opening_hours_id>', methods=['GET'])
@jwt_required()
def get_branch_opening_hours(branch_opening_hours_id):
    # Logic to get branch_opening_hours data
    result = Branch_opening_hours.read(branch_opening_hours_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@branch_opening_hours_bp.route('/', methods=['POST'])
@jwt_required()
def create_branch_opening_hours():
    # Logic to create branch_opening_hours data
    result = Branch_opening_hours.create(branch_id=request.values.get('branch_id'), weekday=request.values.get('weekday'), opens=request.values.get('opens'), closes=request.values.get('closes'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@branch_opening_hours_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_branch_opening_hours(id):
    # Logic to update branch_opening_hours data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Branch_opening_hours.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@branch_opening_hours_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_branch_opening_hours(id):
    # Logic to delete branch_opening_hours data
    result = Branch_opening_hours.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
