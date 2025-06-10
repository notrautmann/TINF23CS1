
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Inventory_locations

non_id_columns = ['warehouse_id', 'code', 'description']

inventory_locations_bp = Blueprint('inventory_locations', __name__, url_prefix='/inventory_locations')

@inventory_locations_bp.route('/<int:inventory_locations_id>', methods=['GET'])
@jwt_required()
def get_inventory_locations(inventory_locations_id):
    # Logic to get inventory_locations data
    result = Inventory_locations.read(inventory_locations_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@inventory_locations_bp.route('/', methods=['POST'])
@jwt_required()
def create_inventory_locations():
    # Logic to create inventory_locations data
    result = Inventory_locations.create(warehouse_id=request.values.get('warehouse_id'), code=request.values.get('code'), description=request.values.get('description'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@inventory_locations_bp.route('/<int:inventory_locations_id>', methods=['PUT'])
@jwt_required()
def update_inventory_locations(inventory_locations_id):
    # Logic to update inventory_locations data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Inventory_locations.update(inventory_locations_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@inventory_locations_bp.route('/<int:inventory_locations_id>', methods=['DELETE'])
@jwt_required()
def delete_inventory_locations(inventory_locations_id):
    # Logic to delete inventory_locations data
    result = Inventory_locations.delete(inventory_locations_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
