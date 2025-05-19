
from flask import Blueprint, jsonify, request
from db import Allergens

non_id_columns = ['code', 'name', 'description']

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
    result = Allergens.create(code=request.values.get('code'), name=request.values.get('name'), description=request.values.get('description'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@allergens_bp.route('/<int:id>', methods=['PUT'])
def update_allergens(id):
    # Logic to update allergens data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Allergens.update(id, **changes)
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
