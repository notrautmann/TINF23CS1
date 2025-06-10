
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Users

non_id_columns = ['username', 'password_hash', 'role_id', 'employee_id', 'is_active', 'created_at', 'updated_at']

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.route('/<int:users_id>', methods=['GET'])
@jwt_required()
def get_users(users_id):
    # Logic to get users data
    result = Users.read(users_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@users_bp.route('/', methods=['POST'])
@jwt_required()
def create_users():
    # Logic to create users data
    result = Users.create(username=request.values.get('username'), password_hash=request.values.get('password_hash'), role_id=request.values.get('role_id'), employee_id=request.values.get('employee_id'), is_active=request.values.get('is_active'), created_at=request.values.get('created_at'), updated_at=request.values.get('updated_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@users_bp.route('/<int:users_id>', methods=['PUT'])
@jwt_required()
def update_users(users_id):
    # Logic to update users data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Users.update(users_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@users_bp.route('/<int:users_id>', methods=['DELETE'])
@jwt_required()
def delete_users(users_id):
    # Logic to delete users data
    result = Users.delete(users_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
