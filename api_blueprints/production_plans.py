
from flask import Blueprint, jsonify, request
from db import Production_plans

production_plans_bp = Blueprint('production_plans', __name__, url_prefix='/production_plans')

@production_plans_bp.route('/<int:id>', methods=['GET'])
def get_production_plans(id):
    # Logic to get production_plans data
    result = Production_plans.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@production_plans_bp.route('/', methods=['POST'])
def create_production_plans():
    # Logic to create production_plans data
    result = Production_plans.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@production_plans_bp.route('/<int:id>', methods=['PUT'])
def update_production_plans(id):
    # Logic to update production_plans data
    result = Production_plans.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@production_plans_bp.route('/<int:id>', methods=['DELETE'])
def delete_production_plans(id):
    # Logic to delete production_plans data
    result = Production_plans.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
