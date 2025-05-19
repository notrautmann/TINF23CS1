
from flask import Blueprint, jsonify, request
from db import Supplier_invoices

supplier_invoices_bp = Blueprint('supplier_invoices', __name__, url_prefix='/supplier_invoices')

@supplier_invoices_bp.route('/<int:id>', methods=['GET'])
def get_supplier_invoices(id):
    # Logic to get supplier_invoices data
    result = Supplier_invoices.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@supplier_invoices_bp.route('/', methods=['POST'])
def create_supplier_invoices():
    # Logic to create supplier_invoices data
    result = Supplier_invoices.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_invoices_bp.route('/<int:id>', methods=['PUT'])
def update_supplier_invoices(id):
    # Logic to update supplier_invoices data
    result = Supplier_invoices.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_invoices_bp.route('/<int:id>', methods=['DELETE'])
def delete_supplier_invoices(id):
    # Logic to delete supplier_invoices data
    result = Supplier_invoices.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
