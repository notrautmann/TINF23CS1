
from flask import Blueprint, jsonify, request
from db import Tax_codes

tax_codes_bp = Blueprint('tax_codes', __name__, url_prefix='/tax_codes')

@tax_codes_bp.route('/<int:id>', methods=['GET'])
def get_tax_codes(id):
    # Logic to get tax_codes data
    result = Tax_codes.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@tax_codes_bp.route('/', methods=['POST'])
def create_tax_codes():
    # Logic to create tax_codes data
    result = Tax_codes.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@tax_codes_bp.route('/<int:id>', methods=['PUT'])
def update_tax_codes(id):
    # Logic to update tax_codes data
    result = Tax_codes.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@tax_codes_bp.route('/<int:id>', methods=['DELETE'])
def delete_tax_codes(id):
    # Logic to delete tax_codes data
    result = Tax_codes.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
