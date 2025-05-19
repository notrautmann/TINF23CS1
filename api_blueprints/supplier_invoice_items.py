
from flask import Blueprint, jsonify, request
from db import Supplier_invoice_items

supplier_invoice_items_bp = Blueprint('supplier_invoice_items', __name__, url_prefix='/supplier_invoice_items')

@supplier_invoice_items_bp.route('/<int:id>', methods=['GET'])
def get_supplier_invoice_items(id):
    # Logic to get supplier_invoice_items data
    result = Supplier_invoice_items.read(id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200
@supplier_invoice_items_bp.route('/', methods=['POST'])
def create_supplier_invoice_items():
    # Logic to create supplier_invoice_items data
    result = Supplier_invoice_items.create(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_invoice_items_bp.route('/<int:id>', methods=['PUT'])
def update_supplier_invoice_items(id):
    # Logic to update supplier_invoice_items data
    result = Supplier_invoice_items.update(request.values())
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
@supplier_invoice_items_bp.route('/<int:id>', methods=['DELETE'])
def delete_supplier_invoice_items(id):
    # Logic to delete supplier_invoice_items data
    result = Supplier_invoice_items.delete(id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
