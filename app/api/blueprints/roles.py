
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Roles

non_id_columns = ['name',
	'description']

roles_bp = Blueprint('roles',
    __name__,
    url_prefix='/roles')

@roles_bp.route('/<int:roles_id>', methods=['GET'])
@jwt_required()
def get_roles(roles_id):
    # Logic to get roles data
    result = Roles.read(roles_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@roles_bp.route('/', methods=['POST'])
@jwt_required()
def create_roles():
    # Logic to create roles data
    result = Roles.create(name=request.values.get('name'),
		description=request.values.get('description'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@roles_bp.route('/<int:roles_id>', methods=['PUT'])
@jwt_required()
def update_roles(roles_id):
    # Logic to update roles data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Roles.update(roles_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@roles_bp.route('/<int:roles_id>', methods=['DELETE'])
@jwt_required()
def delete_roles(roles_id):
    # Logic to delete roles data
    result = Roles.delete(roles_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
