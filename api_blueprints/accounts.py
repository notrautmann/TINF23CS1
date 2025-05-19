
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from db import Accounts

non_id_columns = ['name', 'account_number', 'iban', 'bic', 'description']

accounts_bp = Blueprint('accounts', __name__, url_prefix='/accounts')

@accounts_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_accounts(id):
    # Logic to get accounts data
    result = Accounts.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@accounts_bp.route('/', methods=['POST'])
@jwt_required()
def create_accounts():
    # Logic to create accounts data
    result = Accounts.create(name=request.values.get('name'), account_number=request.values.get('account_number'), iban=request.values.get('iban'), bic=request.values.get('bic'), description=request.values.get('description'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@accounts_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_accounts(id):
    # Logic to update accounts data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Accounts.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@accounts_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_accounts(id):
    # Logic to delete accounts data
    result = Accounts.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
