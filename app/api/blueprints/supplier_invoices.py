
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.db import Supplier_invoices

non_id_columns = ['invoice_number',
	'supplier_id',
	'supplier_order_id',
	'invoice_date',
	'due_date',
	'total_amount',
	'payment_status']

supplier_invoices_bp = Blueprint('supplier_invoices',
    __name__,
    url_prefix='/supplier_invoices')

@supplier_invoices_bp.route('/<int:supplier_invoices_id>', methods=['GET'])
@jwt_required()
def get_supplier_invoices(supplier_invoices_id):
    # Logic to get supplier_invoices data
    result = Supplier_invoices.read(supplier_invoices_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@supplier_invoices_bp.route('/', methods=['POST'])
@jwt_required()
def create_supplier_invoices():
    # Logic to create supplier_invoices data
    result = Supplier_invoices.create(invoice_number=request.values.get('invoice_number'),
		supplier_id=request.values.get('supplier_id'),
		supplier_order_id=request.values.get('supplier_order_id'),
		invoice_date=request.values.get('invoice_date'),
		due_date=request.values.get('due_date'),
		total_amount=request.values.get('total_amount'),
		payment_status=request.values.get('payment_status'))
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@supplier_invoices_bp.route('/<int:supplier_invoices_id>', methods=['PUT'])
@jwt_required()
def update_supplier_invoices(supplier_invoices_id):
    # Logic to update supplier_invoices data
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = Supplier_invoices.update(supplier_invoices_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200

@supplier_invoices_bp.route('/<int:supplier_invoices_id>', methods=['DELETE'])
@jwt_required()
def delete_supplier_invoices(supplier_invoices_id):
    # Logic to delete supplier_invoices data
    result = Supplier_invoices.delete(supplier_invoices_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data':result}), 200
