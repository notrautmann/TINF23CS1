"""
Implements the CRUD-operations for the supplier_order_items-table.

Functions:

    get_supplier_order_items(supplier_order_items_id)
    create_supplier_order_items()
    update_supplier_order_items(supplier_order_items_id)
    delete_supplier_order_items(supplier_order_items_id)

Misc variables:

    supplier_order_items_id
"""
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from app.db.crud import read, create, update, delete
from app.db.records.supplier_order_items import Supplier_order_items

non_id_columns = ['order_id',
    'ingredient_id',
    'qty',
    'unit_price',
    'received_amount',
    'received',
    'received_at',
    'tax_code_id']

supplier_order_items_bp = Blueprint('supplier_order_items',
    __name__,
    url_prefix='/supplier_order_items')

@supplier_order_items_bp.route('/<int:supplier_order_items_id>', methods=['GET'])
@jwt_required()
def get_supplier_order_items(supplier_order_items_id):
    """
    Logic to get supplier_order_items data

    Parameter:
    supplier_order_items_id (int): Id of the supplier_order_items-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = read(Supplier_order_items, id=supplier_order_items_id)
    if result is None:
        return jsonify({'success': False, 'error': 'Not found'}), 404
    return jsonify({'success': True, 'data': result}), 200

@supplier_order_items_bp.route('/', methods=['POST'])
@jwt_required()
def create_supplier_order_items():
    """
    Logic to create supplier_order_items data

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    obj = Supplier_order_items(order_id=request.values.get('order_id'),
        ingredient_id=request.values.get('ingredient_id'),
        qty=request.values.get('qty'),
        unit_price=request.values.get('unit_price'),
        received_amount=request.values.get('received_amount'),
        received=request.values.get('received'),
        received_at=request.values.get('received_at'),
        tax_code_id=request.values.get('tax_code_id'))
    result = create(obj)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data': result}), 200

@supplier_order_items_bp.route('/<int:supplier_order_items_id>', methods=['PUT'])
@jwt_required()
def update_supplier_order_items(supplier_order_items_id):
    """
    Logic to update supplier_order_items data

    Parameter:
        supplier_order_items_id (int): Id of the supplier_order_items-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    changes = {f'{col[0]}': request.values.get(f'{col[0]}')
        for col in non_id_columns if request.values.get(f'{col[0]}') is not None}
    result = update(Supplier_order_items, supplier_order_items_id, **changes)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data': result}), 200

@supplier_order_items_bp.route('/<int:supplier_order_items_id>', methods=['DELETE'])
@jwt_required()
def delete_supplier_order_items(supplier_order_items_id):
    """
    Logic to delete supplier_order_items data

    Parameter:
        supplier_order_items_id (int): Id of the supplier_order_items-object

    Return:
        json-structure: Returns status code and if operation succeeded the returned data
            otherwise an error message
    """
    result = delete(Supplier_order_items, supplier_order_items_id)
    if result is None:
        return jsonify({'success': False, 'error': 'error when writing data'}), 500
    return jsonify({'success': True, 'data': result}), 200
