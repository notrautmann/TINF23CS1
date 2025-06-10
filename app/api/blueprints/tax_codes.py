"""
Implements the CRUD-operations for the tax_codes-table.

Functions:

    get_tax_codes(tax_codes_id)
    create_tax_codes()
    update_tax_codes(tax_codes_id)
    delete_tax_codes(tax_codes_id)

Misc variables:

    tax_codes_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Tax_codes

non_id_columns = ['name',
	'rate',
	'valid_from',
	'valid_to']

tax_codes_bp = Blueprint('tax_codes',
    __name__,
    url_prefix='/tax_codes')

@tax_codes_bp.route('/<int:tax_codes_id>', methods=['GET'])
@jwt_required()
def get_tax_codes(tax_codes_id):
    """
    Logic to get tax_codes data
    
    Parameter:
    tax_codes_id (int): Id of the tax_codes-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Tax_codes.read(tax_codes_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@tax_codes_bp.route('/', methods=['POST'])
@jwt_required()
def create_tax_codes():
    """
    Logic to create tax_codes data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Tax_codes.create(name=request.values.get('name'),
		rate=request.values.get('rate'),
		valid_from=request.values.get('valid_from'),
		valid_to=request.values.get('valid_to'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@tax_codes_bp.route('/<int:tax_codes_id>', methods=['PUT'])
@jwt_required()
def update_tax_codes(tax_codes_id):
    """
    Logic to update tax_codes data
    
    Parameter:
        tax_codes_id (int): Id of the tax_codes-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Tax_codes.update(tax_codes_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@tax_codes_bp.route('/<int:tax_codes_id>', methods=['DELETE'])
@jwt_required()
def delete_tax_codes(tax_codes_id):
    """
    Logic to delete tax_codes data
    
    Parameter:
        tax_codes_id (int): Id of the tax_codes-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Tax_codes.delete(tax_codes_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
