
from flask import Blueprint, jsonify, request
from db import Accounts

accounts_bp = Blueprint('accounts', __name__, url_prefix='/accounts')

@accounts_bp.route('/<int:id>', methods=['GET'])
def get_accounts(id):
    # Logic to get accounts data
    result = Accounts.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@accounts_bp.route('/', methods=['POST'])
def create_accounts():
    # Logic to create accounts data
    result = Accounts.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@accounts_bp.route('/<int:id>', methods=['PUT'])
def update_accounts(id):
    # Logic to update accounts data
    result = Accounts.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@accounts_bp.route('/<int:id>', methods=['DELETE'])
def delete_accounts(id):
    # Logic to delete accounts data
    result = Accounts.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
