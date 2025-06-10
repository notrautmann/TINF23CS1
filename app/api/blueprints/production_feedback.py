"""
Implements the CRUD-operations for the production_feedback-table.

Functions:

    get_production_feedback(production_feedback_id)
    create_production_feedback()
    update_production_feedback(production_feedback_id)
    delete_production_feedback(production_feedback_id)

Misc variables:

    production_feedback_id    
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Production_feedback

non_id_columns = ['plan_item_id',
	'user_id',
	'produced_qty',
	'timestamp']

production_feedback_bp = Blueprint('production_feedback',
    __name__,
    url_prefix='/production_feedback')

@production_feedback_bp.route('/<int:production_feedback_id>', methods=['GET'])
@jwt_required()
def get_production_feedback(production_feedback_id):
    """
    Logic to get production_feedback data
    
    Parameter:
    production_feedback_id (int): Id of the production_feedback-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Production_feedback.read(production_feedback_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@production_feedback_bp.route('/', methods=['POST'])
@jwt_required()
def create_production_feedback():
    """
    Logic to create production_feedback data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Production_feedback.create(plan_item_id=request.values.get('plan_item_id'),
		user_id=request.values.get('user_id'),
		produced_qty=request.values.get('produced_qty'),
		timestamp=request.values.get('timestamp'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@production_feedback_bp.route('/<int:production_feedback_id>', methods=['PUT'])
@jwt_required()
def update_production_feedback(production_feedback_id):
    """
    Logic to update production_feedback data
    
    Parameter:
        production_feedback_id (int): Id of the production_feedback-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Production_feedback.update(production_feedback_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@production_feedback_bp.route('/<int:production_feedback_id>', methods=['DELETE'])
@jwt_required()
def delete_production_feedback(production_feedback_id):
    """
    Logic to delete production_feedback data
    
    Parameter:
        production_feedback_id (int): Id of the production_feedback-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = Production_feedback.delete(production_feedback_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
