
from flask import Blueprint, jsonify, request
from db import Inventory_locations

non_id_columns = ['warehouse_id', 'code', 'description']

inventory_locations_bp = Blueprint('inventory_locations', __name__, url_prefix='/inventory_locations')

@inventory_locations_bp.route('/<int:id>', methods=['GET'])
def get_inventory_locations(id):
    # Logic to get inventory_locations data
    result = Inventory_locations.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@inventory_locations_bp.route('/', methods=['POST'])
def create_inventory_locations():
    # Logic to create inventory_locations data
    result = Inventory_locations.create(warehouse_id=request.values.get('warehouse_id'), code=request.values.get('code'), description=request.values.get('description'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@inventory_locations_bp.route('/<int:id>', methods=['PUT'])
def update_inventory_locations(id):
    # Logic to update inventory_locations data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Inventory_locations.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@inventory_locations_bp.route('/<int:id>', methods=['DELETE'])
def delete_inventory_locations(id):
    # Logic to delete inventory_locations data
    result = Inventory_locations.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
