
from flask import Blueprint, jsonify, request
from db import Branches

branches_bp = Blueprint('branches', __name__, url_prefix='/branches')

@branches_bp.route('/<int:id>', methods=['GET'])
def get_branches(id):
    # Logic to get branches data
    result = Branches.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@branches_bp.route('/', methods=['POST'])
def create_branches():
    # Logic to create branches data
    result = Branches.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@branches_bp.route('/<int:id>', methods=['PUT'])
def update_branches(id):
    # Logic to update branches data
    result = Branches.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@branches_bp.route('/<int:id>', methods=['DELETE'])
def delete_branches(id):
    # Logic to delete branches data
    result = Branches.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
