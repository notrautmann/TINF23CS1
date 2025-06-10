"""
Generator Script for generating API routes and logic for all database tables
"""
import sys
# allow imports when running script from within project dir
#sys.path.append('.')

from pathlib import Path
from create_db import get_table_names, get_columns_for_table
from environment_constants import API_BLUEPRINTS_PATH

def generate():
    """
    Main function for generating the app/api/blueprint files.
    """
    tables = get_table_names()
    for table in tables:
        output_path = Path.joinpath(API_BLUEPRINTS_PATH, f"{table}.py")
        output_path.parent.mkdir(exist_ok=True, parents=True)
        with open(output_path, "w") as f:
            f.write(generate_routes_file_for_table(table))

def generate_routes_file_for_table(table):
    """
    Main Code that includes CRUD-operations for all blueprint files/database tables.

    Parameters:
        table (any): The name of the table in the database
    Return:
        f-string: The code for the CRUD operations for every table
    """
    new_line = "\n"
    tab = "\t"
    columns = get_columns_for_table(table)
    non_id_columns = [col for col in columns if col[0] != "id"]
    code = f"""\"\"\"
Implements the CRUD-operations for the {table}-table.

Functions:

    get_{table}({table}_id)
    create_{table}()
    update_{table}({table}_id)
    delete_{table}({table}_id)

Misc variables:

    {table}_id    
\"\"\"
    
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import {table.capitalize()}

non_id_columns = {"["+f",{new_line}{tab}".join([f"'{col[0]}'" for col in non_id_columns])+"]"}

{table}_bp = Blueprint('{table}',
    __name__,
    url_prefix='/{table}')

@{table}_bp.route('/<int:{table}_id>', methods=['GET'])
@jwt_required()
def get_{table}({table}_id):
    \"\"\"
    Logic to get {table} data
    
    Parameter:
    {table}_id (int): Id of the {table}-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    \"\"\"
    result = {table.capitalize()}.read({table}_id)
    if result is None:
        return jsonify({{'success': False, 'error': 'Not found'}}), 404
    return jsonify({{'success': True, 'data': result}}), 200

@{table}_bp.route('/', methods=['POST'])
@jwt_required()
def create_{table}():
    \"\"\"
    Logic to create {table} data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    \"\"\"
    result = {table.capitalize()}.create({f',{new_line}{tab}{tab}'.join([f"{col[0]}=request.values.get('{col[0]}')" for col in non_id_columns])})
    if result is None:
        return jsonify({{'success': False, 'error': 'error when writing data'}}), 500
    return jsonify({{'success': True, 'data':result}}), 200

@{table}_bp.route('/<int:{table}_id>', methods=['PUT'])
@jwt_required()
def update_{table}({table}_id):
    \"\"\"
    Logic to update {table} data
    
    Parameter:
        {table}_id (int): Id of the {table}-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    \"\"\"
    {get_changes_line()}
    result = {table.capitalize()}.update({table}_id, **changes)
    if result is None:
        return jsonify({{'success': False, 'error': 'error when writing data'}}), 500
    return jsonify({{'success': True, 'data':result}}), 200

@{table}_bp.route('/<int:{table}_id>', methods=['DELETE'])
@jwt_required()
def delete_{table}({table}_id):
    \"\"\"
    Logic to delete {table} data
    
    Parameter:
        {table}_id (int): Id of the {table}-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data otherwise an error message
    \"\"\"
    result = {table.capitalize()}.delete({table}_id)
    if result is None:
        return jsonify({{'success': False, 'error': 'error when writing data'}}), 500
    return jsonify({{'success': True, 'data':result}}), 200
"""
    return code

def get_changes_line():
    """
    Returns the line number where changes happened

    Return:
        string: changes line number
    """
    return """changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}"""

if __name__ == "__main__":  
    generate()
    print("API routes generated successfully.")
