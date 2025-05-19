
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from db import Roles

non_id_columns = ['name', 'description']

roles_bp = Blueprint('roles', __name__, url_prefix='/roles')

@roles_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_roles(id):
    # Logic to get roles data
    result = Roles.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@roles_bp.route('/', methods=['POST'])
@jwt_required()
def create_roles():
    # Logic to create roles data
    result = Roles.create(name=request.values.get('name'), description=request.values.get('description'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@roles_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_roles(id):
    # Logic to update roles data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Roles.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@roles_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_roles(id):
    # Logic to delete roles data
    result = Roles.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
