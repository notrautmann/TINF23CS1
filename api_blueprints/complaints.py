
from flask import Blueprint, jsonify, request
from db import Complaints

complaints_bp = Blueprint('complaints', __name__, url_prefix='/complaints')

@complaints_bp.route('/<int:id>', methods=['GET'])
def get_complaints(id):
    # Logic to get complaints data
    result = Complaints.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@complaints_bp.route('/', methods=['POST'])
def create_complaints():
    # Logic to create complaints data
    result = Complaints.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@complaints_bp.route('/<int:id>', methods=['PUT'])
def update_complaints(id):
    # Logic to update complaints data
    result = Complaints.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@complaints_bp.route('/<int:id>', methods=['DELETE'])
def delete_complaints(id):
    # Logic to delete complaints data
    result = Complaints.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
