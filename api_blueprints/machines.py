
from flask import Blueprint, jsonify, request
from db import Machines

machines_bp = Blueprint('machines', __name__, url_prefix='/machines')

@machines_bp.route('/<int:id>', methods=['GET'])
def get_machines(id):
    # Logic to get machines data
    result = Machines.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@machines_bp.route('/', methods=['POST'])
def create_machines():
    # Logic to create machines data
    result = Machines.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@machines_bp.route('/<int:id>', methods=['PUT'])
def update_machines(id):
    # Logic to update machines data
    result = Machines.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@machines_bp.route('/<int:id>', methods=['DELETE'])
def delete_machines(id):
    # Logic to delete machines data
    result = Machines.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
