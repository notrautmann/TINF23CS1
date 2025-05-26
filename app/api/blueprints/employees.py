
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Employees

non_id_columns = ['first_name', 'last_name', 'email', 'phone', 'hire_date', 'termination_date', 'hourly_wage', 'monthly_salary', 'created_at', 'updated_at']

employees_bp = Blueprint('employees', __name__, url_prefix='/employees')

@employees_bp.route('/<int:employees_id>', methods=['GET'])
@jwt_required()
def get_employees(employees_id):
    # Logic to get employees data
    result = Employees.read(employees_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@employees_bp.route('/', methods=['POST'])
@jwt_required()
def create_employees():
    # Logic to create employees data
    result = Employees.create(first_name=request.values.get('first_name'), last_name=request.values.get('last_name'), email=request.values.get('email'), phone=request.values.get('phone'), hire_date=request.values.get('hire_date'), termination_date=request.values.get('termination_date'), hourly_wage=request.values.get('hourly_wage'), monthly_salary=request.values.get('monthly_salary'), created_at=request.values.get('created_at'), updated_at=request.values.get('updated_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@employees_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_employees(id):
    # Logic to update employees data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}') for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Employees.update(id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@employees_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_employees(id):
    # Logic to delete employees data
    result = Employees.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
