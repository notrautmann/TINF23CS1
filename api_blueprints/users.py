
from flask import Blueprint, jsonify, request
from db import Users

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
    result = Users.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@users_bp.route('/<int:id>', methods=['PUT'])
def update_users(id):
    # Logic to update users data
    result = Users.update(request.values())
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
