
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from db import Production_plan_items

non_id_columns = ['plan_id', 'product_id', 'planned_qty', 'produced_qty']

production_plan_items_bp = Blueprint('production_plan_items', __name__, url_prefix='/production_plan_items')

@production_plan_items_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_production_plan_items(id):
    # Logic to get production_plan_items data
    result = Production_plan_items.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@production_plan_items_bp.route('/', methods=['POST'])
@jwt_required()
def create_production_plan_items():
    # Logic to create production_plan_items data
    result = Production_plan_items.create(plan_id=request.values.get('plan_id'), product_id=request.values.get('product_id'), planned_qty=request.values.get('planned_qty'), produced_qty=request.values.get('produced_qty'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@production_plan_items_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_production_plan_items(id):
    # Logic to update production_plan_items data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Production_plan_items.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@production_plan_items_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_production_plan_items(id):
    # Logic to delete production_plan_items data
    result = Production_plan_items.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
