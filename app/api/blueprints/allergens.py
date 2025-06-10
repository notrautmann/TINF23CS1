"""
Implements the CRUD-operations for the allergens-table.

Functions:

    get_allergens(allergens_id)
    create_allergens()
    update_allergens(allergens_id)
    delete_allergens(allergens_id)

Misc variables:

    allergens_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.records.allergens import Allergens

non_id_columns = ['code',
	'name',
	'description']

allergens_bp = Blueprint('allergens',
    __name__,
    url_prefix='/allergens')

@allergens_bp.route('/<int:allergens_id>', methods=['GET'])
@jwt_required()
def get_allergens(allergens_id):
    """
    Logic to get allergens data
    
    Parameter:
    allergens_id (int): Id of the allergens-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Allergens.read(allergens_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@allergens_bp.route('/', methods=['POST'])
@jwt_required()
def create_allergens():
    """
    Logic to create allergens data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Allergens.create(code=request.values.get('code'),
		name=request.values.get('name'),
		description=request.values.get('description'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@allergens_bp.route('/<int:allergens_id>', methods=['PUT'])
@jwt_required()
def update_allergens(allergens_id):
    """
    Logic to update allergens data
    
    Parameter:
        allergens_id (int): Id of the allergens-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Allergens.update(allergens_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@allergens_bp.route('/<int:allergens_id>', methods=['DELETE'])
@jwt_required()
def delete_allergens(allergens_id):
    """
    Logic to delete allergens data
    
    Parameter:
        allergens_id (int): Id of the allergens-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Allergens.delete(allergens_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
