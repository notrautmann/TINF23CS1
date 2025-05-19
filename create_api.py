from pathlib import Path
from create_db import get_table_names
def generate():
    
    tables = get_table_names()
    for table in tables:
        output_path = Path(f"api_blueprints/{table}.py")
        output_path.parent.mkdir(exist_ok=True, parents=True)
        with open(output_path, "w") as f:
            f.write(generate_routes_file_for_table(table))

def generate_routes_file_for_table(table):
    open = "{"
    close = "}"

    code = f"""
from flask import Blueprint, jsonify, request
from db import {table.capitalize()}

{table}_bp = Blueprint('{table}', __name__, url_prefix='/{table}')

@{table}_bp.route('/<int:id>', methods=['GET'])
def get_{table}(id):
    # Logic to get {table} data
    result = {table.capitalize()}.read(id)
    if result is None:
        return jsonify({{'success': False, 'error': 'Not found'}}), 404
    return jsonify({{'success': True, 'data': result}}), 200
@{table}_bp.route('/', methods=['POST'])
def create_{table}():
    # Logic to create {table} data
    result = {table.capitalize()}.create(request.values())
    if result is None:
        return jsonify({{'success': False, 'error': 'error when writing data'}}), 500
    return jsonify({{'success': True, 'data':result}}), 200
@{table}_bp.route('/<int:id>', methods=['PUT'])
def update_{table}(id):
    # Logic to update {table} data
    result = {table.capitalize()}.update(request.values())
    if result is None:
        return jsonify({{'success': False, 'error': 'error when writing data'}}), 500
    return jsonify({{'success': True, 'data':result}}), 200
@{table}_bp.route('/<int:id>', methods=['DELETE'])
def delete_{table}(id):
    # Logic to delete {table} data
    result = {table.capitalize()}.delete(id)
    if result is None:
        return jsonify({{'success': False, 'error': 'error when writing data'}}), 500
    return jsonify({{'success': True, 'data':result}}), 200
"""
    return code

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
