
from flask import Blueprint, jsonify, request
from db import Roles

roles_bp = Blueprint('roles', __name__, url_prefix='/roles')

@roles_bp.route('/<int:id>', methods=['GET'])
def get_roles(id):
    # Logic to get roles data
    result = Roles.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@roles_bp.route('/', methods=['POST'])
def create_roles():
    # Logic to create roles data
    result = Roles.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@roles_bp.route('/<int:id>', methods=['PUT'])
def update_roles(id):
    # Logic to update roles data
    result = Roles.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@roles_bp.route('/<int:id>', methods=['DELETE'])
def delete_roles(id):
    # Logic to delete roles data
    result = Roles.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
