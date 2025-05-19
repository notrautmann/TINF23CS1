
from flask import Blueprint, jsonify, request
from db import Suppliers

suppliers_bp = Blueprint('suppliers', __name__, url_prefix='/suppliers')

@suppliers_bp.route('/<int:id>', methods=['GET'])
def get_suppliers(id):
    # Logic to get suppliers data
    result = Suppliers.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@suppliers_bp.route('/', methods=['POST'])
def create_suppliers():
    # Logic to create suppliers data
    result = Suppliers.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@suppliers_bp.route('/<int:id>', methods=['PUT'])
def update_suppliers(id):
    # Logic to update suppliers data
    result = Suppliers.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@suppliers_bp.route('/<int:id>', methods=['DELETE'])
def delete_suppliers(id):
    # Logic to delete suppliers data
    result = Suppliers.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
