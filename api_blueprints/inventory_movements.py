
from flask import Blueprint, jsonify, request
from db import Inventory_movements

inventory_movements_bp = Blueprint('inventory_movements', __name__, url_prefix='/inventory_movements')

@inventory_movements_bp.route('/<int:id>', methods=['GET'])
def get_inventory_movements(id):
    # Logic to get inventory_movements data
    result = Inventory_movements.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@inventory_movements_bp.route('/', methods=['POST'])
def create_inventory_movements():
    # Logic to create inventory_movements data
    result = Inventory_movements.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@inventory_movements_bp.route('/<int:id>', methods=['PUT'])
def update_inventory_movements(id):
    # Logic to update inventory_movements data
    result = Inventory_movements.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@inventory_movements_bp.route('/<int:id>', methods=['DELETE'])
def delete_inventory_movements(id):
    # Logic to delete inventory_movements data
    result = Inventory_movements.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
