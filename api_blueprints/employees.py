
from flask import Blueprint, jsonify, request
from db import Employees

employees_bp = Blueprint('employees', __name__, url_prefix='/employees')

@employees_bp.route('/<int:id>', methods=['GET'])
def get_employees(id):
    # Logic to get employees data
    result = Employees.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@employees_bp.route('/', methods=['POST'])
def create_employees():
    # Logic to create employees data
    result = Employees.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@employees_bp.route('/<int:id>', methods=['PUT'])
def update_employees(id):
    # Logic to update employees data
    result = Employees.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@employees_bp.route('/<int:id>', methods=['DELETE'])
def delete_employees(id):
    # Logic to delete employees data
    result = Employees.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
