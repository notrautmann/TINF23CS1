import db
from flask import Flask, request, jsonify
app = Flask(__name__)

# API routes
# branch_order_window
@app.route('/branch_order_window/<int:id>', methods=['GET'])
def get_branch_order_window(id):
    # Logic to get branch_order_window data
    return jsonify(db.Branch_order_window.read(id), status=200, mimetype='application/json')

@app.route('/branch_order_window', methods=['POST'])
def create_branch_order_window():
    # Logic to create branch_order_window data
    db.Branch_order_window.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/branch_order_window/<int:id>', methods=['PUT'])
def update_branch_order_window(id):
    # Logic to update branch_order_window data
    db.Branch_order_window.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/branch_order_window/<int:id>', methods=['DELETE'])
def delete_branch_order_window(id):
    # Logic to delete branch_order_window data
    db.Branch_order_window.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# employees
@app.route('/employees/<int:id>', methods=['GET'])
def get_employees(id):
    # Logic to get employees data
    return jsonify(db.Employees.read(id), status=200, mimetype='application/json')

@app.route('/employees', methods=['POST'])
def create_employees():
    # Logic to create employees data
    db.Employees.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employees(id):
    # Logic to update employees data
    db.Employees.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employees(id):
    # Logic to delete employees data
    db.Employees.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# employee_time_entries
@app.route('/employee_time_entries/<int:id>', methods=['GET'])
def get_employee_time_entries(id):
    # Logic to get employee_time_entries data
    return jsonify(db.Employee_time_entries.read(id), status=200, mimetype='application/json')

@app.route('/employee_time_entries', methods=['POST'])
def create_employee_time_entries():
    # Logic to create employee_time_entries data
    db.Employee_time_entries.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/employee_time_entries/<int:id>', methods=['PUT'])
def update_employee_time_entries(id):
    # Logic to update employee_time_entries data
    db.Employee_time_entries.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/employee_time_entries/<int:id>', methods=['DELETE'])
def delete_employee_time_entries(id):
    # Logic to delete employee_time_entries data
    db.Employee_time_entries.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# payment_methods
@app.route('/payment_methods/<int:id>', methods=['GET'])
def get_payment_methods(id):
    # Logic to get payment_methods data
    return jsonify(db.Payment_methods.read(id), status=200, mimetype='application/json')

@app.route('/payment_methods', methods=['POST'])
def create_payment_methods():
    # Logic to create payment_methods data
    db.Payment_methods.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/payment_methods/<int:id>', methods=['PUT'])
def update_payment_methods(id):
    # Logic to update payment_methods data
    db.Payment_methods.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/payment_methods/<int:id>', methods=['DELETE'])
def delete_payment_methods(id):
    # Logic to delete payment_methods data
    db.Payment_methods.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# accounts
@app.route('/accounts/<int:id>', methods=['GET'])
def get_accounts(id):
    # Logic to get accounts data
    return jsonify(db.Accounts.read(id), status=200, mimetype='application/json')

@app.route('/accounts', methods=['POST'])
def create_accounts():
    # Logic to create accounts data
    db.Accounts.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/accounts/<int:id>', methods=['PUT'])
def update_accounts(id):
    # Logic to update accounts data
    db.Accounts.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/accounts/<int:id>', methods=['DELETE'])
def delete_accounts(id):
    # Logic to delete accounts data
    db.Accounts.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# branches
@app.route('/branches/<int:id>', methods=['GET'])
def get_branches(id):
    # Logic to get branches data
    return jsonify(db.Branches.read(id), status=200, mimetype='application/json')

@app.route('/branches', methods=['POST'])
def create_branches():
    # Logic to create branches data
    db.Branches.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/branches/<int:id>', methods=['PUT'])
def update_branches(id):
    # Logic to update branches data
    db.Branches.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/branches/<int:id>', methods=['DELETE'])
def delete_branches(id):
    # Logic to delete branches data
    db.Branches.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# roles
@app.route('/roles/<int:id>', methods=['GET'])
def get_roles(id):
    # Logic to get roles data
    return jsonify(db.Roles.read(id), status=200, mimetype='application/json')

@app.route('/roles', methods=['POST'])
def create_roles():
    # Logic to create roles data
    db.Roles.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/roles/<int:id>', methods=['PUT'])
def update_roles(id):
    # Logic to update roles data
    db.Roles.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/roles/<int:id>', methods=['DELETE'])
def delete_roles(id):
    # Logic to delete roles data
    db.Roles.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# users
@app.route('/users/<int:id>', methods=['GET'])
def get_users(id):
    # Logic to get users data
    return jsonify(db.Users.read(id), status=200, mimetype='application/json')

@app.route('/users', methods=['POST'])
def create_users():
    # Logic to create users data
    db.Users.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/users/<int:id>', methods=['PUT'])
def update_users(id):
    # Logic to update users data
    db.Users.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_users(id):
    # Logic to delete users data
    db.Users.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# ingredient_allergens
@app.route('/ingredient_allergens/<int:id>', methods=['GET'])
def get_ingredient_allergens(id):
    # Logic to get ingredient_allergens data
    return jsonify(db.Ingredient_allergens.read(id), status=200, mimetype='application/json')

@app.route('/ingredient_allergens', methods=['POST'])
def create_ingredient_allergens():
    # Logic to create ingredient_allergens data
    db.Ingredient_allergens.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/ingredient_allergens/<int:id>', methods=['PUT'])
def update_ingredient_allergens(id):
    # Logic to update ingredient_allergens data
    db.Ingredient_allergens.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/ingredient_allergens/<int:id>', methods=['DELETE'])
def delete_ingredient_allergens(id):
    # Logic to delete ingredient_allergens data
    db.Ingredient_allergens.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# allergens
@app.route('/allergens/<int:id>', methods=['GET'])
def get_allergens(id):
    # Logic to get allergens data
    return jsonify(db.Allergens.read(id), status=200, mimetype='application/json')

@app.route('/allergens', methods=['POST'])
def create_allergens():
    # Logic to create allergens data
    db.Allergens.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/allergens/<int:id>', methods=['PUT'])
def update_allergens(id):
    # Logic to update allergens data
    db.Allergens.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/allergens/<int:id>', methods=['DELETE'])
def delete_allergens(id):
    # Logic to delete allergens data
    db.Allergens.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# suppliers
@app.route('/suppliers/<int:id>', methods=['GET'])
def get_suppliers(id):
    # Logic to get suppliers data
    return jsonify(db.Suppliers.read(id), status=200, mimetype='application/json')

@app.route('/suppliers', methods=['POST'])
def create_suppliers():
    # Logic to create suppliers data
    db.Suppliers.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/suppliers/<int:id>', methods=['PUT'])
def update_suppliers(id):
    # Logic to update suppliers data
    db.Suppliers.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/suppliers/<int:id>', methods=['DELETE'])
def delete_suppliers(id):
    # Logic to delete suppliers data
    db.Suppliers.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# products
@app.route('/products/<int:id>', methods=['GET'])
def get_products(id):
    # Logic to get products data
    return jsonify(db.Products.read(id), status=200, mimetype='application/json')

@app.route('/products', methods=['POST'])
def create_products():
    # Logic to create products data
    db.Products.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/products/<int:id>', methods=['PUT'])
def update_products(id):
    # Logic to update products data
    db.Products.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_products(id):
    # Logic to delete products data
    db.Products.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# product_allergens
@app.route('/product_allergens/<int:id>', methods=['GET'])
def get_product_allergens(id):
    # Logic to get product_allergens data
    return jsonify(db.Product_allergens.read(id), status=200, mimetype='application/json')

@app.route('/product_allergens', methods=['POST'])
def create_product_allergens():
    # Logic to create product_allergens data
    db.Product_allergens.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/product_allergens/<int:id>', methods=['PUT'])
def update_product_allergens(id):
    # Logic to update product_allergens data
    db.Product_allergens.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/product_allergens/<int:id>', methods=['DELETE'])
def delete_product_allergens(id):
    # Logic to delete product_allergens data
    db.Product_allergens.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# inventory_locations
@app.route('/inventory_locations/<int:id>', methods=['GET'])
def get_inventory_locations(id):
    # Logic to get inventory_locations data
    return jsonify(db.Inventory_locations.read(id), status=200, mimetype='application/json')

@app.route('/inventory_locations', methods=['POST'])
def create_inventory_locations():
    # Logic to create inventory_locations data
    db.Inventory_locations.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/inventory_locations/<int:id>', methods=['PUT'])
def update_inventory_locations(id):
    # Logic to update inventory_locations data
    db.Inventory_locations.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/inventory_locations/<int:id>', methods=['DELETE'])
def delete_inventory_locations(id):
    # Logic to delete inventory_locations data
    db.Inventory_locations.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# inventory_movements
@app.route('/inventory_movements/<int:id>', methods=['GET'])
def get_inventory_movements(id):
    # Logic to get inventory_movements data
    return jsonify(db.Inventory_movements.read(id), status=200, mimetype='application/json')

@app.route('/inventory_movements', methods=['POST'])
def create_inventory_movements():
    # Logic to create inventory_movements data
    db.Inventory_movements.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/inventory_movements/<int:id>', methods=['PUT'])
def update_inventory_movements(id):
    # Logic to update inventory_movements data
    db.Inventory_movements.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/inventory_movements/<int:id>', methods=['DELETE'])
def delete_inventory_movements(id):
    # Logic to delete inventory_movements data
    db.Inventory_movements.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# supplier_products
@app.route('/supplier_products/<int:id>', methods=['GET'])
def get_supplier_products(id):
    # Logic to get supplier_products data
    return jsonify(db.Supplier_products.read(id), status=200, mimetype='application/json')

@app.route('/supplier_products', methods=['POST'])
def create_supplier_products():
    # Logic to create supplier_products data
    db.Supplier_products.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/supplier_products/<int:id>', methods=['PUT'])
def update_supplier_products(id):
    # Logic to update supplier_products data
    db.Supplier_products.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/supplier_products/<int:id>', methods=['DELETE'])
def delete_supplier_products(id):
    # Logic to delete supplier_products data
    db.Supplier_products.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# recipes
@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipes(id):
    # Logic to get recipes data
    return jsonify(db.Recipes.read(id), status=200, mimetype='application/json')

@app.route('/recipes', methods=['POST'])
def create_recipes():
    # Logic to create recipes data
    db.Recipes.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipes(id):
    # Logic to update recipes data
    db.Recipes.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipes(id):
    # Logic to delete recipes data
    db.Recipes.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# warehouses
@app.route('/warehouses/<int:id>', methods=['GET'])
def get_warehouses(id):
    # Logic to get warehouses data
    return jsonify(db.Warehouses.read(id), status=200, mimetype='application/json')

@app.route('/warehouses', methods=['POST'])
def create_warehouses():
    # Logic to create warehouses data
    db.Warehouses.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/warehouses/<int:id>', methods=['PUT'])
def update_warehouses(id):
    # Logic to update warehouses data
    db.Warehouses.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/warehouses/<int:id>', methods=['DELETE'])
def delete_warehouses(id):
    # Logic to delete warehouses data
    db.Warehouses.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# customer_order_items
@app.route('/customer_order_items/<int:id>', methods=['GET'])
def get_customer_order_items(id):
    # Logic to get customer_order_items data
    return jsonify(db.Customer_order_items.read(id), status=200, mimetype='application/json')

@app.route('/customer_order_items', methods=['POST'])
def create_customer_order_items():
    # Logic to create customer_order_items data
    db.Customer_order_items.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/customer_order_items/<int:id>', methods=['PUT'])
def update_customer_order_items(id):
    # Logic to update customer_order_items data
    db.Customer_order_items.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/customer_order_items/<int:id>', methods=['DELETE'])
def delete_customer_order_items(id):
    # Logic to delete customer_order_items data
    db.Customer_order_items.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# sales_receipt_items
@app.route('/sales_receipt_items/<int:id>', methods=['GET'])
def get_sales_receipt_items(id):
    # Logic to get sales_receipt_items data
    return jsonify(db.Sales_receipt_items.read(id), status=200, mimetype='application/json')

@app.route('/sales_receipt_items', methods=['POST'])
def create_sales_receipt_items():
    # Logic to create sales_receipt_items data
    db.Sales_receipt_items.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/sales_receipt_items/<int:id>', methods=['PUT'])
def update_sales_receipt_items(id):
    # Logic to update sales_receipt_items data
    db.Sales_receipt_items.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/sales_receipt_items/<int:id>', methods=['DELETE'])
def delete_sales_receipt_items(id):
    # Logic to delete sales_receipt_items data
    db.Sales_receipt_items.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# complaints
@app.route('/complaints/<int:id>', methods=['GET'])
def get_complaints(id):
    # Logic to get complaints data
    return jsonify(db.Complaints.read(id), status=200, mimetype='application/json')

@app.route('/complaints', methods=['POST'])
def create_complaints():
    # Logic to create complaints data
    db.Complaints.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/complaints/<int:id>', methods=['PUT'])
def update_complaints(id):
    # Logic to update complaints data
    db.Complaints.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/complaints/<int:id>', methods=['DELETE'])
def delete_complaints(id):
    # Logic to delete complaints data
    db.Complaints.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# customers
@app.route('/customers/<int:id>', methods=['GET'])
def get_customers(id):
    # Logic to get customers data
    return jsonify(db.Customers.read(id), status=200, mimetype='application/json')

@app.route('/customers', methods=['POST'])
def create_customers():
    # Logic to create customers data
    db.Customers.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/customers/<int:id>', methods=['PUT'])
def update_customers(id):
    # Logic to update customers data
    db.Customers.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customers(id):
    # Logic to delete customers data
    db.Customers.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# sales_receipts
@app.route('/sales_receipts/<int:id>', methods=['GET'])
def get_sales_receipts(id):
    # Logic to get sales_receipts data
    return jsonify(db.Sales_receipts.read(id), status=200, mimetype='application/json')

@app.route('/sales_receipts', methods=['POST'])
def create_sales_receipts():
    # Logic to create sales_receipts data
    db.Sales_receipts.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/sales_receipts/<int:id>', methods=['PUT'])
def update_sales_receipts(id):
    # Logic to update sales_receipts data
    db.Sales_receipts.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/sales_receipts/<int:id>', methods=['DELETE'])
def delete_sales_receipts(id):
    # Logic to delete sales_receipts data
    db.Sales_receipts.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# customer_feedback
@app.route('/customer_feedback/<int:id>', methods=['GET'])
def get_customer_feedback(id):
    # Logic to get customer_feedback data
    return jsonify(db.Customer_feedback.read(id), status=200, mimetype='application/json')

@app.route('/customer_feedback', methods=['POST'])
def create_customer_feedback():
    # Logic to create customer_feedback data
    db.Customer_feedback.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/customer_feedback/<int:id>', methods=['PUT'])
def update_customer_feedback(id):
    # Logic to update customer_feedback data
    db.Customer_feedback.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/customer_feedback/<int:id>', methods=['DELETE'])
def delete_customer_feedback(id):
    # Logic to delete customer_feedback data
    db.Customer_feedback.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# shift_schedule
@app.route('/shift_schedule/<int:id>', methods=['GET'])
def get_shift_schedule(id):
    # Logic to get shift_schedule data
    return jsonify(db.Shift_schedule.read(id), status=200, mimetype='application/json')

@app.route('/shift_schedule', methods=['POST'])
def create_shift_schedule():
    # Logic to create shift_schedule data
    db.Shift_schedule.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/shift_schedule/<int:id>', methods=['PUT'])
def update_shift_schedule(id):
    # Logic to update shift_schedule data
    db.Shift_schedule.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/shift_schedule/<int:id>', methods=['DELETE'])
def delete_shift_schedule(id):
    # Logic to delete shift_schedule data
    db.Shift_schedule.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# production_feedback
@app.route('/production_feedback/<int:id>', methods=['GET'])
def get_production_feedback(id):
    # Logic to get production_feedback data
    return jsonify(db.Production_feedback.read(id), status=200, mimetype='application/json')

@app.route('/production_feedback', methods=['POST'])
def create_production_feedback():
    # Logic to create production_feedback data
    db.Production_feedback.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/production_feedback/<int:id>', methods=['PUT'])
def update_production_feedback(id):
    # Logic to update production_feedback data
    db.Production_feedback.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/production_feedback/<int:id>', methods=['DELETE'])
def delete_production_feedback(id):
    # Logic to delete production_feedback data
    db.Production_feedback.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# shifts
@app.route('/shifts/<int:id>', methods=['GET'])
def get_shifts(id):
    # Logic to get shifts data
    return jsonify(db.Shifts.read(id), status=200, mimetype='application/json')

@app.route('/shifts', methods=['POST'])
def create_shifts():
    # Logic to create shifts data
    db.Shifts.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/shifts/<int:id>', methods=['PUT'])
def update_shifts(id):
    # Logic to update shifts data
    db.Shifts.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/shifts/<int:id>', methods=['DELETE'])
def delete_shifts(id):
    # Logic to delete shifts data
    db.Shifts.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# supplier_order_items
@app.route('/supplier_order_items/<int:id>', methods=['GET'])
def get_supplier_order_items(id):
    # Logic to get supplier_order_items data
    return jsonify(db.Supplier_order_items.read(id), status=200, mimetype='application/json')

@app.route('/supplier_order_items', methods=['POST'])
def create_supplier_order_items():
    # Logic to create supplier_order_items data
    db.Supplier_order_items.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/supplier_order_items/<int:id>', methods=['PUT'])
def update_supplier_order_items(id):
    # Logic to update supplier_order_items data
    db.Supplier_order_items.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/supplier_order_items/<int:id>', methods=['DELETE'])
def delete_supplier_order_items(id):
    # Logic to delete supplier_order_items data
    db.Supplier_order_items.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# goods_receipt_items
@app.route('/goods_receipt_items/<int:id>', methods=['GET'])
def get_goods_receipt_items(id):
    # Logic to get goods_receipt_items data
    return jsonify(db.Goods_receipt_items.read(id), status=200, mimetype='application/json')

@app.route('/goods_receipt_items', methods=['POST'])
def create_goods_receipt_items():
    # Logic to create goods_receipt_items data
    db.Goods_receipt_items.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/goods_receipt_items/<int:id>', methods=['PUT'])
def update_goods_receipt_items(id):
    # Logic to update goods_receipt_items data
    db.Goods_receipt_items.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/goods_receipt_items/<int:id>', methods=['DELETE'])
def delete_goods_receipt_items(id):
    # Logic to delete goods_receipt_items data
    db.Goods_receipt_items.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# supplier_invoice_items
@app.route('/supplier_invoice_items/<int:id>', methods=['GET'])
def get_supplier_invoice_items(id):
    # Logic to get supplier_invoice_items data
    return jsonify(db.Supplier_invoice_items.read(id), status=200, mimetype='application/json')

@app.route('/supplier_invoice_items', methods=['POST'])
def create_supplier_invoice_items():
    # Logic to create supplier_invoice_items data
    db.Supplier_invoice_items.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/supplier_invoice_items/<int:id>', methods=['PUT'])
def update_supplier_invoice_items(id):
    # Logic to update supplier_invoice_items data
    db.Supplier_invoice_items.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/supplier_invoice_items/<int:id>', methods=['DELETE'])
def delete_supplier_invoice_items(id):
    # Logic to delete supplier_invoice_items data
    db.Supplier_invoice_items.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# refund_reasons
@app.route('/refund_reasons/<int:id>', methods=['GET'])
def get_refund_reasons(id):
    # Logic to get refund_reasons data
    return jsonify(db.Refund_reasons.read(id), status=200, mimetype='application/json')

@app.route('/refund_reasons', methods=['POST'])
def create_refund_reasons():
    # Logic to create refund_reasons data
    db.Refund_reasons.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/refund_reasons/<int:id>', methods=['PUT'])
def update_refund_reasons(id):
    # Logic to update refund_reasons data
    db.Refund_reasons.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/refund_reasons/<int:id>', methods=['DELETE'])
def delete_refund_reasons(id):
    # Logic to delete refund_reasons data
    db.Refund_reasons.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# supplier_orders
@app.route('/supplier_orders/<int:id>', methods=['GET'])
def get_supplier_orders(id):
    # Logic to get supplier_orders data
    return jsonify(db.Supplier_orders.read(id), status=200, mimetype='application/json')

@app.route('/supplier_orders', methods=['POST'])
def create_supplier_orders():
    # Logic to create supplier_orders data
    db.Supplier_orders.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/supplier_orders/<int:id>', methods=['PUT'])
def update_supplier_orders(id):
    # Logic to update supplier_orders data
    db.Supplier_orders.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/supplier_orders/<int:id>', methods=['DELETE'])
def delete_supplier_orders(id):
    # Logic to delete supplier_orders data
    db.Supplier_orders.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# pos_terminals
@app.route('/pos_terminals/<int:id>', methods=['GET'])
def get_pos_terminals(id):
    # Logic to get pos_terminals data
    return jsonify(db.Pos_terminals.read(id), status=200, mimetype='application/json')

@app.route('/pos_terminals', methods=['POST'])
def create_pos_terminals():
    # Logic to create pos_terminals data
    db.Pos_terminals.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/pos_terminals/<int:id>', methods=['PUT'])
def update_pos_terminals(id):
    # Logic to update pos_terminals data
    db.Pos_terminals.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/pos_terminals/<int:id>', methods=['DELETE'])
def delete_pos_terminals(id):
    # Logic to delete pos_terminals data
    db.Pos_terminals.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# goods_receipts
@app.route('/goods_receipts/<int:id>', methods=['GET'])
def get_goods_receipts(id):
    # Logic to get goods_receipts data
    return jsonify(db.Goods_receipts.read(id), status=200, mimetype='application/json')

@app.route('/goods_receipts', methods=['POST'])
def create_goods_receipts():
    # Logic to create goods_receipts data
    db.Goods_receipts.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/goods_receipts/<int:id>', methods=['PUT'])
def update_goods_receipts(id):
    # Logic to update goods_receipts data
    db.Goods_receipts.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/goods_receipts/<int:id>', methods=['DELETE'])
def delete_goods_receipts(id):
    # Logic to delete goods_receipts data
    db.Goods_receipts.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# supplier_invoices
@app.route('/supplier_invoices/<int:id>', methods=['GET'])
def get_supplier_invoices(id):
    # Logic to get supplier_invoices data
    return jsonify(db.Supplier_invoices.read(id), status=200, mimetype='application/json')

@app.route('/supplier_invoices', methods=['POST'])
def create_supplier_invoices():
    # Logic to create supplier_invoices data
    db.Supplier_invoices.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/supplier_invoices/<int:id>', methods=['PUT'])
def update_supplier_invoices(id):
    # Logic to update supplier_invoices data
    db.Supplier_invoices.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/supplier_invoices/<int:id>', methods=['DELETE'])
def delete_supplier_invoices(id):
    # Logic to delete supplier_invoices data
    db.Supplier_invoices.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# payment_transactions
@app.route('/payment_transactions/<int:id>', methods=['GET'])
def get_payment_transactions(id):
    # Logic to get payment_transactions data
    return jsonify(db.Payment_transactions.read(id), status=200, mimetype='application/json')

@app.route('/payment_transactions', methods=['POST'])
def create_payment_transactions():
    # Logic to create payment_transactions data
    db.Payment_transactions.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/payment_transactions/<int:id>', methods=['PUT'])
def update_payment_transactions(id):
    # Logic to update payment_transactions data
    db.Payment_transactions.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/payment_transactions/<int:id>', methods=['DELETE'])
def delete_payment_transactions(id):
    # Logic to delete payment_transactions data
    db.Payment_transactions.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# machines
@app.route('/machines/<int:id>', methods=['GET'])
def get_machines(id):
    # Logic to get machines data
    return jsonify(db.Machines.read(id), status=200, mimetype='application/json')

@app.route('/machines', methods=['POST'])
def create_machines():
    # Logic to create machines data
    db.Machines.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/machines/<int:id>', methods=['PUT'])
def update_machines(id):
    # Logic to update machines data
    db.Machines.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/machines/<int:id>', methods=['DELETE'])
def delete_machines(id):
    # Logic to delete machines data
    db.Machines.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# branch_opening_hours
@app.route('/branch_opening_hours/<int:id>', methods=['GET'])
def get_branch_opening_hours(id):
    # Logic to get branch_opening_hours data
    return jsonify(db.Branch_opening_hours.read(id), status=200, mimetype='application/json')

@app.route('/branch_opening_hours', methods=['POST'])
def create_branch_opening_hours():
    # Logic to create branch_opening_hours data
    db.Branch_opening_hours.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/branch_opening_hours/<int:id>', methods=['PUT'])
def update_branch_opening_hours(id):
    # Logic to update branch_opening_hours data
    db.Branch_opening_hours.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/branch_opening_hours/<int:id>', methods=['DELETE'])
def delete_branch_opening_hours(id):
    # Logic to delete branch_opening_hours data
    db.Branch_opening_hours.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# tax_codes
@app.route('/tax_codes/<int:id>', methods=['GET'])
def get_tax_codes(id):
    # Logic to get tax_codes data
    return jsonify(db.Tax_codes.read(id), status=200, mimetype='application/json')

@app.route('/tax_codes', methods=['POST'])
def create_tax_codes():
    # Logic to create tax_codes data
    db.Tax_codes.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/tax_codes/<int:id>', methods=['PUT'])
def update_tax_codes(id):
    # Logic to update tax_codes data
    db.Tax_codes.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/tax_codes/<int:id>', methods=['DELETE'])
def delete_tax_codes(id):
    # Logic to delete tax_codes data
    db.Tax_codes.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# ingredients
@app.route('/ingredients/<int:id>', methods=['GET'])
def get_ingredients(id):
    # Logic to get ingredients data
    return jsonify(db.Ingredients.read(id), status=200, mimetype='application/json')

@app.route('/ingredients', methods=['POST'])
def create_ingredients():
    # Logic to create ingredients data
    db.Ingredients.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/ingredients/<int:id>', methods=['PUT'])
def update_ingredients(id):
    # Logic to update ingredients data
    db.Ingredients.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/ingredients/<int:id>', methods=['DELETE'])
def delete_ingredients(id):
    # Logic to delete ingredients data
    db.Ingredients.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# recipe_items
@app.route('/recipe_items/<int:id>', methods=['GET'])
def get_recipe_items(id):
    # Logic to get recipe_items data
    return jsonify(db.Recipe_items.read(id), status=200, mimetype='application/json')

@app.route('/recipe_items', methods=['POST'])
def create_recipe_items():
    # Logic to create recipe_items data
    db.Recipe_items.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/recipe_items/<int:id>', methods=['PUT'])
def update_recipe_items(id):
    # Logic to update recipe_items data
    db.Recipe_items.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/recipe_items/<int:id>', methods=['DELETE'])
def delete_recipe_items(id):
    # Logic to delete recipe_items data
    db.Recipe_items.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# customer_orders
@app.route('/customer_orders/<int:id>', methods=['GET'])
def get_customer_orders(id):
    # Logic to get customer_orders data
    return jsonify(db.Customer_orders.read(id), status=200, mimetype='application/json')

@app.route('/customer_orders', methods=['POST'])
def create_customer_orders():
    # Logic to create customer_orders data
    db.Customer_orders.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/customer_orders/<int:id>', methods=['PUT'])
def update_customer_orders(id):
    # Logic to update customer_orders data
    db.Customer_orders.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/customer_orders/<int:id>', methods=['DELETE'])
def delete_customer_orders(id):
    # Logic to delete customer_orders data
    db.Customer_orders.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# production_plans
@app.route('/production_plans/<int:id>', methods=['GET'])
def get_production_plans(id):
    # Logic to get production_plans data
    return jsonify(db.Production_plans.read(id), status=200, mimetype='application/json')

@app.route('/production_plans', methods=['POST'])
def create_production_plans():
    # Logic to create production_plans data
    db.Production_plans.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/production_plans/<int:id>', methods=['PUT'])
def update_production_plans(id):
    # Logic to update production_plans data
    db.Production_plans.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/production_plans/<int:id>', methods=['DELETE'])
def delete_production_plans(id):
    # Logic to delete production_plans data
    db.Production_plans.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# production_plan_items
@app.route('/production_plan_items/<int:id>', methods=['GET'])
def get_production_plan_items(id):
    # Logic to get production_plan_items data
    return jsonify(db.Production_plan_items.read(id), status=200, mimetype='application/json')

@app.route('/production_plan_items', methods=['POST'])
def create_production_plan_items():
    # Logic to create production_plan_items data
    db.Production_plan_items.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/production_plan_items/<int:id>', methods=['PUT'])
def update_production_plan_items(id):
    # Logic to update production_plan_items data
    db.Production_plan_items.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/production_plan_items/<int:id>', methods=['DELETE'])
def delete_production_plan_items(id):
    # Logic to delete production_plan_items data
    db.Production_plan_items.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# refunds
@app.route('/refunds/<int:id>', methods=['GET'])
def get_refunds(id):
    # Logic to get refunds data
    return jsonify(db.Refunds.read(id), status=200, mimetype='application/json')

@app.route('/refunds', methods=['POST'])
def create_refunds():
    # Logic to create refunds data
    db.Refunds.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/refunds/<int:id>', methods=['PUT'])
def update_refunds(id):
    # Logic to update refunds data
    db.Refunds.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/refunds/<int:id>', methods=['DELETE'])
def delete_refunds(id):
    # Logic to delete refunds data
    db.Refunds.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')

# refund_items
@app.route('/refund_items/<int:id>', methods=['GET'])
def get_refund_items(id):
    # Logic to get refund_items data
    return jsonify(db.Refund_items.read(id), status=200, mimetype='application/json')

@app.route('/refund_items', methods=['POST'])
def create_refund_items():
    # Logic to create refund_items data
    db.Refund_items.create(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/refund_items/<int:id>', methods=['PUT'])
def update_refund_items(id):
    # Logic to update refund_items data
    db.Refund_items.update(request.values())
    return jsonify({'success': True}, status=200, mimetype='application/json')

@app.route('/refund_items/<int:id>', methods=['DELETE'])
def delete_refund_items(id):
    # Logic to delete refund_items data
    db.Refund_items.delete(id)
    return jsonify({'success': True}, status=200, mimetype='application/json')


