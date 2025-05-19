
from flask import Blueprint, jsonify, request
from db import Production_plan_items

production_plan_items_bp = Blueprint('production_plan_items', __name__, url_prefix='/production_plan_items')

@production_plan_items_bp.route('/<int:id>', methods=['GET'])
def get_production_plan_items(id):
    # Logic to get production_plan_items data
    result = Production_plan_items.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@production_plan_items_bp.route('/', methods=['POST'])
def create_production_plan_items():
    # Logic to create production_plan_items data
    result = Production_plan_items.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@production_plan_items_bp.route('/<int:id>', methods=['PUT'])
def update_production_plan_items(id):
    # Logic to update production_plan_items data
    result = Production_plan_items.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@production_plan_items_bp.route('/<int:id>', methods=['DELETE'])
def delete_production_plan_items(id):
    # Logic to delete production_plan_items data
    result = Production_plan_items.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
