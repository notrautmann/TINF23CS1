
from flask import Blueprint, jsonify, request
from db import Inventory_locations

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
    result = Inventory_locations.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@inventory_locations_bp.route('/<int:id>', methods=['PUT'])
def update_inventory_locations(id):
    # Logic to update inventory_locations data
    result = Inventory_locations.update(request.values())
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
