
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Production_plans

non_id_columns = ['branch_id', 'planned_date', 'status', 'created_at', 'updated_at']

production_plans_bp = Blueprint('production_plans', __name__, url_prefix='/production_plans')

@production_plans_bp.route('/<int:production_plans_id>', methods=['GET'])
@jwt_required()
def get_production_plans(production_plans_id):
    # Logic to get production_plans data
    result = Production_plans.read(production_plans_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@production_plans_bp.route('/', methods=['POST'])
@jwt_required()
def create_production_plans():
    # Logic to create production_plans data
    result = Production_plans.create(branch_id=request.values.get('branch_id'), planned_date=request.values.get('planned_date'), status=request.values.get('status'), created_at=request.values.get('created_at'), updated_at=request.values.get('updated_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@production_plans_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_production_plans(id):
    # Logic to update production_plans data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Production_plans.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@production_plans_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_production_plans(id):
    # Logic to delete production_plans data
    result = Production_plans.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
