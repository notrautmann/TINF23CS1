
from flask import Blueprint, jsonify, request
from db import Allergens

allergens_bp = Blueprint('allergens', __name__, url_prefix='/allergens')

@allergens_bp.route('/<int:id>', methods=['GET'])
def get_allergens(id):
    # Logic to get allergens data
    result = Allergens.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@allergens_bp.route('/', methods=['POST'])
def create_allergens():
    # Logic to create allergens data
    result = Allergens.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@allergens_bp.route('/<int:id>', methods=['PUT'])
def update_allergens(id):
    # Logic to update allergens data
    result = Allergens.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@allergens_bp.route('/<int:id>', methods=['DELETE'])
def delete_allergens(id):
    # Logic to delete allergens data
    result = Allergens.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
