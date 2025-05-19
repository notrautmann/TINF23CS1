
from flask import Blueprint, jsonify, request
from db import Pos_terminals

pos_terminals_bp = Blueprint('pos_terminals', __name__, url_prefix='/pos_terminals')

@pos_terminals_bp.route('/<int:id>', methods=['GET'])
def get_pos_terminals(id):
    # Logic to get pos_terminals data
    result = Pos_terminals.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@pos_terminals_bp.route('/', methods=['POST'])
def create_pos_terminals():
    # Logic to create pos_terminals data
    result = Pos_terminals.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@pos_terminals_bp.route('/<int:id>', methods=['PUT'])
def update_pos_terminals(id):
    # Logic to update pos_terminals data
    result = Pos_terminals.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@pos_terminals_bp.route('/<int:id>', methods=['DELETE'])
def delete_pos_terminals(id):
    # Logic to delete pos_terminals data
    result = Pos_terminals.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
