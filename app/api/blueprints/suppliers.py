
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Suppliers

non_id_columns = ['name',
	'contact_name',
	'email',
	'phone',
	'address_line',
	'postal_code',
	'city',
	'country',
	'created_at',
	'updated_at']

suppliers_bp = Blueprint('suppliers',
    __name__,
    url_prefix='/suppliers')

@suppliers_bp.route('/<int:suppliers_id>', methods=['GET'])
@jwt_required()
def get_suppliers(suppliers_id):
    # Logic to get suppliers data
    result = Suppliers.read(suppliers_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@suppliers_bp.route('/', methods=['POST'])
@jwt_required()
def create_suppliers():
    # Logic to create suppliers data
    result = Suppliers.create(name=request.values.get('name'),
		contact_name=request.values.get('contact_name'),
		email=request.values.get('email'),
		phone=request.values.get('phone'),
		address_line=request.values.get('address_line'),
		postal_code=request.values.get('postal_code'),
		city=request.values.get('city'),
		country=request.values.get('country'),
		created_at=request.values.get('created_at'),
		updated_at=request.values.get('updated_at'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@suppliers_bp.route('/<int:suppliers_id>', methods=['PUT'])
@jwt_required()
def update_suppliers(suppliers_id):
    # Logic to update suppliers data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Suppliers.update(suppliers_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@suppliers_bp.route('/<int:suppliers_id>', methods=['DELETE'])
@jwt_required()
def delete_suppliers(suppliers_id):
    # Logic to delete suppliers data
    result = Suppliers.delete(suppliers_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
