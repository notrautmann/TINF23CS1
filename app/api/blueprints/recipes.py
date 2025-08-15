"""
Implements the CRUD-operations for the recipes-table.

Functions:

    get_recipes(recipes_id)
    create_recipes()
    update_recipes(recipes_id)
    delete_recipes(recipes_id)

Misc variables:

    recipes_id
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.crud import read, create, update, delete
from app.db.records.recipes import Recipes

non_id_columns = ['name',
    'description',
    'created_at',
    'updated_at']

recipes_bp = Blueprint('recipes',
    __name__,
    url_prefix='/recipes')

@recipes_bp.route('/<int:recipes_id>', methods=['GET'])
@jwt_required()
def get_recipes(recipes_id):
    """
    Logic to get recipes data

    Parameter:
    recipes_id (int): Id of the recipes-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = read(Recipes, id=recipes_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@recipes_bp.route('/', methods=['POST'])
@jwt_required()
def create_recipes():
    """
    Logic to create recipes data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    recipe_obj = Recipes(name=request.values.get('name'),
        description=request.values.get('description'),
        created_at=request.values.get('created_at'),
        updated_at=request.values.get('updated_at'))
    result = create(recipe_obj)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data': result}), 200

@recipes_bp.route('/<int:recipes_id>', methods=['PUT'])
@jwt_required()
def update_recipes(recipes_id):
    """
    Logic to update recipes data

    Parameter:
        recipes_id (int): Id of the recipes-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = update(Recipes, recipes_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data': result}), 200

@recipes_bp.route('/<int:recipes_id>', methods=['DELETE'])
@jwt_required()
def delete_recipes(recipes_id):
    """
    Logic to delete recipes data

    Parameter:
        recipes_id (int): Id of the recipes-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = delete(Recipes, recipes_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data': result}), 200
