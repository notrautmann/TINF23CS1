
from flask import Blueprint, jsonify, request
from db import Users

non_id_columns = ['username', 'password_hash', 'role_id', 'employee_id', 'is_active', 'created_at', 'updated_at']

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/<int:id>', methods=['GET'])
def get_users(id):
    # Logic to get users data
    result = Users.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@users_bp.route('/', methods=['POST'])
def create_users():
    # Logic to create users data
    result = Users.create(username=request.values.get('username'), password_hash=request.values.get('password_hash'), role_id=request.values.get('role_id'), employee_id=request.values.get('employee_id'), is_active=request.values.get('is_active'), created_at=request.values.get('created_at'), updated_at=request.values.get('updated_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@users_bp.route('/<int:id>', methods=['PUT'])
def update_users(id):
    # Logic to update users data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Users.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@users_bp.route('/<int:id>', methods=['DELETE'])
def delete_users(id):
    # Logic to delete users data
    result = Users.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
