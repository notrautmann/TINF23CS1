
from flask import Blueprint, jsonify, request
from db import Production_feedback

production_feedback_bp = Blueprint('production_feedback', __name__, url_prefix='/production_feedback')

@production_feedback_bp.route('/<int:id>', methods=['GET'])
def get_production_feedback(id):
    # Logic to get production_feedback data
    result = Production_feedback.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@production_feedback_bp.route('/', methods=['POST'])
def create_production_feedback():
    # Logic to create production_feedback data
    result = Production_feedback.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@production_feedback_bp.route('/<int:id>', methods=['PUT'])
def update_production_feedback(id):
    # Logic to update production_feedback data
    result = Production_feedback.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@production_feedback_bp.route('/<int:id>', methods=['DELETE'])
def delete_production_feedback(id):
    # Logic to delete production_feedback data
    result = Production_feedback.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
