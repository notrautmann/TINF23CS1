
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from db import Warehouses

non_id_columns = ['branch_id', 'name', 'description']

warehouses_bp = Blueprint('warehouses', __name__, url_prefix='/warehouses')

@warehouses_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_warehouses(id):
    # Logic to get warehouses data
    result = Warehouses.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@warehouses_bp.route('/', methods=['POST'])
@jwt_required()
def create_warehouses():
    # Logic to create warehouses data
    result = Warehouses.create(branch_id=request.values.get('branch_id'), name=request.values.get('name'), description=request.values.get('description'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@warehouses_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_warehouses(id):
    # Logic to update warehouses data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Warehouses.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@warehouses_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_warehouses(id):
    # Logic to delete warehouses data
    result = Warehouses.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
