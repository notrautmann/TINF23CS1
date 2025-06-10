
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Pos_terminals

non_id_columns = ['branch_id', 'terminal_code', 'description', 'is_active']

pos_terminals_bp = Blueprint('pos_terminals', __name__, url_prefix='/pos_terminals')

@pos_terminals_bp.route('/<int:pos_terminals_id>', methods=['GET'])
@jwt_required()
def get_pos_terminals(pos_terminals_id):
    # Logic to get pos_terminals data
    result = Pos_terminals.read(pos_terminals_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@pos_terminals_bp.route('/', methods=['POST'])
@jwt_required()
def create_pos_terminals():
    # Logic to create pos_terminals data
    result = Pos_terminals.create(branch_id=request.values.get('branch_id'), terminal_code=request.values.get('terminal_code'), description=request.values.get('description'), is_active=request.values.get('is_active'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@pos_terminals_bp.route('/<int:pos_terminals_id>', methods=['PUT'])
@jwt_required()
def update_pos_terminals(pos_terminals_id):
    # Logic to update pos_terminals data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Pos_terminals.update(pos_terminals_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@pos_terminals_bp.route('/<int:pos_terminals_id>', methods=['DELETE'])
@jwt_required()
def delete_pos_terminals(pos_terminals_id):
    # Logic to delete pos_terminals data
    result = Pos_terminals.delete(pos_terminals_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
