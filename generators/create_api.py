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
    
    tables = get_table_names()
    for table in tables:
        output_path = Path.joinpath(API_BLUEPRINTS_PATH, f"{table}.py")
        output_path.parent.mkdir(exist_ok=True, parents=True)
        with open(output_path, "w") as f:
            f.write(generate_routes_file_for_table(table))

def generate_routes_file_for_table(table):

    NEW_LINE = "\n"
    TAB = "\t"
    columns = get_columns_for_table(table)
    non_id_columns = [col for col in columns if col[0] != "id"]
    code = f"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import {table.capitalize()}

non_id_columns = {"["+f",{NEW_LINE}{TAB}".join([f"'{col[0]}'" for col in non_id_columns])+"]"}

{table}_bp = Blueprint('{table}',
    __name__,
    url_prefix='/{table}')

@{table}_bp.route('/<int:{table}_id>', methods=['GET'])
@jwt_required()
def get_{table}({table}_id):
    # Logic to get {table} data
    result = {table.capitalize()}.read({table}_id)
    if result is None:
        return jsonify({{'success': False, 'error': 'Not found'}}), 404
    return jsonify({{'success': True, 'data': result}}), 200

@{table}_bp.route('/', methods=['POST'])
@jwt_required()
def create_{table}():
    # Logic to create {table} data
    result = {table.capitalize()}.create({f',{NEW_LINE}{TAB}{TAB}'.join([f"{col[0]}=request.values.get('{col[0]}')" for col in non_id_columns])})
    if result is None:
        return jsonify({{'success': False, 'error': 'error when writing data'}}), 500
    return jsonify({{'success': True, 'data':result}}), 200

@{table}_bp.route('/<int:{table}_id>', methods=['PUT'])
@jwt_required()
def update_{table}({table}_id):
    # Logic to update {table} data
    {get_changes_line()}
    result = {table.capitalize()}.update({table}_id, **changes)
    if result is None:
        return jsonify({{'success': False, 'error': 'error when writing data'}}), 500
    return jsonify({{'success': True, 'data':result}}), 200

@{table}_bp.route('/<int:{table}_id>', methods=['DELETE'])
@jwt_required()
def delete_{table}({table}_id):
    # Logic to delete {table} data
    result = {table.capitalize()}.delete({table}_id)
    if result is None:
        return jsonify({{'success': False, 'error': 'error when writing data'}}), 500
    return jsonify({{'success': True, 'data':result}}), 200
"""
    return code

def get_changes_line():
    return """changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}"""

def generate_result_check(function_call):
    return f"""
    result = {function_call}
    if result is None:
        return jsonify({{'error': 'Not found'}}, status=404, mimetype='application/json')
    return jsonify(result, status=200, mimetype='application/json')
"""

if __name__ == "__main__":  
    generate()
    print("API routes generated successfully.")
