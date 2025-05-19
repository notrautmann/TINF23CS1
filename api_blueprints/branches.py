
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from db import Branches

non_id_columns = ['name', 'address_line', 'postal_code', 'city', 'country', 'phone', 'email', 'opening_note', 'created_at', 'updated_at']

branches_bp = Blueprint('branches', __name__, url_prefix='/branches')

@branches_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_branches(id):
    # Logic to get branches data
    result = Branches.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@branches_bp.route('/', methods=['POST'])
@jwt_required()
def create_branches():
    # Logic to create branches data
    result = Branches.create(name=request.values.get('name'), address_line=request.values.get('address_line'), postal_code=request.values.get('postal_code'), city=request.values.get('city'), country=request.values.get('country'), phone=request.values.get('phone'), email=request.values.get('email'), opening_note=request.values.get('opening_note'), created_at=request.values.get('created_at'), updated_at=request.values.get('updated_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@branches_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_branches(id):
    # Logic to update branches data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Branches.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@branches_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_branches(id):
    # Logic to delete branches data
    result = Branches.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
