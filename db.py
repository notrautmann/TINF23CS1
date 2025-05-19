import psycopg

from main import connect


class Branch_order_window:
    def __init__(self, id: int = None, branch_id: int = None, weekday: int = None, order_start: str = None, order_end: str = None):
        self.id = id
        self.branch_id = branch_id
        self.weekday = weekday
        self.order_start = order_start
        self.order_end = order_end

    @staticmethod
    def create(branch_id: int, weekday: int, order_start: str, order_end: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO branch_order_window (branch_id, weekday, order_start, order_end) VALUES (%s, %s, %s, %s) RETURNING *", (branch_id, weekday, order_start, order_end,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM branch_order_window WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE branch_order_window SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM branch_order_window WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Employees:
    def __init__(self, id: int = None, first_name: str = None, last_name: str = None, email: str = None, phone: str = None, hire_date: str = None, termination_date: str = None, hourly_wage: float = None, monthly_salary: float = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.hire_date = hire_date
        self.termination_date = termination_date
        self.hourly_wage = hourly_wage
        self.monthly_salary = monthly_salary
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(first_name: str, last_name: str, email: str, phone: str, hire_date: str, termination_date: str, hourly_wage: float, monthly_salary: float, created_at: str, updated_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO employees (first_name, last_name, email, phone, hire_date, termination_date, hourly_wage, monthly_salary, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *", (first_name, last_name, email, phone, hire_date, termination_date, hourly_wage, monthly_salary, created_at, updated_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM employees WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE employees SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM employees WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Employee_time_entries:
    def __init__(self, id: int = None, employee_id: int = None, branch_id: int = None, clock_in: str = None, clock_out: str = None, break_minutes: int = None):
        self.id = id
        self.employee_id = employee_id
        self.branch_id = branch_id
        self.clock_in = clock_in
        self.clock_out = clock_out
        self.break_minutes = break_minutes

    @staticmethod
    def create(employee_id: int, branch_id: int, clock_in: str, clock_out: str, break_minutes: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO employee_time_entries (employee_id, branch_id, clock_in, clock_out, break_minutes) VALUES (%s, %s, %s, %s, %s) RETURNING *", (employee_id, branch_id, clock_in, clock_out, break_minutes,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM employee_time_entries WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE employee_time_entries SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM employee_time_entries WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Payment_methods:
    def __init__(self, id: int = None, name: str = None, external_code: str = None, is_cash: bool = None):
        self.id = id
        self.name = name
        self.external_code = external_code
        self.is_cash = is_cash

    @staticmethod
    def create(name: str, external_code: str, is_cash: bool) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO payment_methods (name, external_code, is_cash) VALUES (%s, %s, %s) RETURNING *", (name, external_code, is_cash,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM payment_methods WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE payment_methods SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM payment_methods WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Accounts:
    def __init__(self, id: int = None, name: str = None, account_number: str = None, iban: str = None, bic: str = None, description: str = None):
        self.id = id
        self.name = name
        self.account_number = account_number
        self.iban = iban
        self.bic = bic
        self.description = description

    @staticmethod
    def create(name: str, account_number: str, iban: str, bic: str, description: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO accounts (name, account_number, iban, bic, description) VALUES (%s, %s, %s, %s, %s) RETURNING *", (name, account_number, iban, bic, description,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM accounts WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE accounts SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM accounts WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Branches:
    def __init__(self, id: int = None, name: str = None, address_line: str = None, postal_code: str = None, city: str = None, country: str = None, phone: str = None, email: str = None, opening_note: str = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.name = name
        self.address_line = address_line
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.phone = phone
        self.email = email
        self.opening_note = opening_note
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(name: str, address_line: str, postal_code: str, city: str, country: str, phone: str, email: str, opening_note: str, created_at: str, updated_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO branches (name, address_line, postal_code, city, country, phone, email, opening_note, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *", (name, address_line, postal_code, city, country, phone, email, opening_note, created_at, updated_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM branches WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE branches SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM branches WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Roles:
    def __init__(self, id: int = None, name: str = None, description: str = None):
        self.id = id
        self.name = name
        self.description = description

    @staticmethod
    def create(name: str, description: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO roles (name, description) VALUES (%s, %s) RETURNING *", (name, description,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM roles WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE roles SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM roles WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Users:
    def __init__(self, id: int = None, username: str = None, password_hash: str = None, role_id: int = None, employee_id: int = None, is_active: bool = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.role_id = role_id
        self.employee_id = employee_id
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(username: str, password_hash: str, role_id: int, employee_id: int, is_active: bool, created_at: str, updated_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (username, password_hash, role_id, employee_id, is_active, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *", (username, password_hash, role_id, employee_id, is_active, created_at, updated_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE users SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM users WHERE id = %s", (id,))
            conn.commit()
        conn.close()

    @staticmethod
    def read_username(username: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT id, username, password_hash, role_id, is_active FROM users WHERE username = %s", (username,))
            row = cur.fetchone()
        conn.close()
        return row


class Ingredient_allergens:
    def __init__(self, ingredient_id: int = None, allergen_id: int = None):
        self.ingredient_id = ingredient_id
        self.allergen_id = allergen_id

    @staticmethod
    def create(ingredient_id: int, allergen_id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO ingredient_allergens (ingredient_id, allergen_id) VALUES (%s, %s) RETURNING *", (ingredient_id, allergen_id,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM ingredient_allergens WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE ingredient_allergens SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM ingredient_allergens WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Allergens:
    def __init__(self, id: int = None, code: str = None, name: str = None, description: str = None):
        self.id = id
        self.code = code
        self.name = name
        self.description = description

    @staticmethod
    def create(code: str, name: str, description: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO allergens (code, name, description) VALUES (%s, %s, %s) RETURNING *", (code, name, description,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM allergens WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE allergens SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM allergens WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Suppliers:
    def __init__(self, id: int = None, name: str = None, contact_name: str = None, email: str = None, phone: str = None, address_line: str = None, postal_code: str = None, city: str = None, country: str = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.name = name
        self.contact_name = contact_name
        self.email = email
        self.phone = phone
        self.address_line = address_line
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(name: str, contact_name: str, email: str, phone: str, address_line: str, postal_code: str, city: str, country: str, created_at: str, updated_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO suppliers (name, contact_name, email, phone, address_line, postal_code, city, country, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *", (name, contact_name, email, phone, address_line, postal_code, city, country, created_at, updated_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM suppliers WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE suppliers SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM suppliers WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Products:
    def __init__(self, id: int = None, name: str = None, sku: str = None, recipe_id: int = None, sales_price: float = None, tax_code_id: int = None, is_active: bool = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.name = name
        self.sku = sku
        self.recipe_id = recipe_id
        self.sales_price = sales_price
        self.tax_code_id = tax_code_id
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(name: str, sku: str, recipe_id: int, sales_price: float, tax_code_id: int, is_active: bool, created_at: str, updated_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO products (name, sku, recipe_id, sales_price, tax_code_id, is_active, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *", (name, sku, recipe_id, sales_price, tax_code_id, is_active, created_at, updated_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM products WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE products SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM products WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Product_allergens:
    def __init__(self, product_id: int = None, allergen_id: int = None):
        self.product_id = product_id
        self.allergen_id = allergen_id

    @staticmethod
    def create(product_id: int, allergen_id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO product_allergens (product_id, allergen_id) VALUES (%s, %s) RETURNING *", (product_id, allergen_id,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM product_allergens WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE product_allergens SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM product_allergens WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Inventory_locations:
    def __init__(self, id: int = None, warehouse_id: int = None, code: str = None, description: str = None):
        self.id = id
        self.warehouse_id = warehouse_id
        self.code = code
        self.description = description

    @staticmethod
    def create(warehouse_id: int, code: str, description: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO inventory_locations (warehouse_id, code, description) VALUES (%s, %s, %s) RETURNING *", (warehouse_id, code, description,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM inventory_locations WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE inventory_locations SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM inventory_locations WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Inventory_movements:
    def __init__(self, id: int = None, movement_type: str = None, ingredient_id: int = None, qty: float = None, unit: str = None, from_location_id: int = None, to_location_id: int = None, reference_type: str = None, reference_id: int = None, created_at: str = None, user_id: int = None):
        self.id = id
        self.movement_type = movement_type
        self.ingredient_id = ingredient_id
        self.qty = qty
        self.unit = unit
        self.from_location_id = from_location_id
        self.to_location_id = to_location_id
        self.reference_type = reference_type
        self.reference_id = reference_id
        self.created_at = created_at
        self.user_id = user_id

    @staticmethod
    def create(movement_type: str, ingredient_id: int, qty: float, unit: str, from_location_id: int, to_location_id: int, reference_type: str, reference_id: int, created_at: str, user_id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO inventory_movements (movement_type, ingredient_id, qty, unit, from_location_id, to_location_id, reference_type, reference_id, created_at, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *", (movement_type, ingredient_id, qty, unit, from_location_id, to_location_id, reference_type, reference_id, created_at, user_id,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM inventory_movements WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE inventory_movements SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM inventory_movements WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Supplier_products:
    def __init__(self, id: int = None, supplier_id: int = None, ingredient_id: int = None, supplier_sku: str = None, purchase_price: float = None, min_order_qty: float = None, lead_time_days: int = None):
        self.id = id
        self.supplier_id = supplier_id
        self.ingredient_id = ingredient_id
        self.supplier_sku = supplier_sku
        self.purchase_price = purchase_price
        self.min_order_qty = min_order_qty
        self.lead_time_days = lead_time_days

    @staticmethod
    def create(supplier_id: int, ingredient_id: int, supplier_sku: str, purchase_price: float, min_order_qty: float, lead_time_days: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO supplier_products (supplier_id, ingredient_id, supplier_sku, purchase_price, min_order_qty, lead_time_days) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *", (supplier_id, ingredient_id, supplier_sku, purchase_price, min_order_qty, lead_time_days,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM supplier_products WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE supplier_products SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM supplier_products WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Recipes:
    def __init__(self, id: int = None, name: str = None, description: str = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(name: str, description: str, created_at: str, updated_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO recipes (name, description, created_at, updated_at) VALUES (%s, %s, %s, %s) RETURNING *", (name, description, created_at, updated_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM recipes WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE recipes SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM recipes WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Warehouses:
    def __init__(self, id: int = None, branch_id: int = None, name: str = None, description: str = None):
        self.id = id
        self.branch_id = branch_id
        self.name = name
        self.description = description

    @staticmethod
    def create(branch_id: int, name: str, description: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO warehouses (branch_id, name, description) VALUES (%s, %s, %s) RETURNING *", (branch_id, name, description,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM warehouses WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE warehouses SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM warehouses WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Customer_order_items:
    def __init__(self, id: int = None, order_id: int = None, product_id: int = None, quantity: int = None, unit_price: float = None, tax_code_id: int = None):
        self.id = id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.tax_code_id = tax_code_id

    @staticmethod
    def create(order_id: int, product_id: int, quantity: int, unit_price: float, tax_code_id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO customer_order_items (order_id, product_id, quantity, unit_price, tax_code_id) VALUES (%s, %s, %s, %s, %s) RETURNING *", (order_id, product_id, quantity, unit_price, tax_code_id,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM customer_order_items WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE customer_order_items SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM customer_order_items WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Sales_receipt_items:
    def __init__(self, id: int = None, receipt_id: int = None, product_id: int = None, qty: float = None, unit_price: float = None, tax_code_id: int = None):
        self.id = id
        self.receipt_id = receipt_id
        self.product_id = product_id
        self.qty = qty
        self.unit_price = unit_price
        self.tax_code_id = tax_code_id

    @staticmethod
    def create(receipt_id: int, product_id: int, qty: float, unit_price: float, tax_code_id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO sales_receipt_items (receipt_id, product_id, qty, unit_price, tax_code_id) VALUES (%s, %s, %s, %s, %s) RETURNING *", (receipt_id, product_id, qty, unit_price, tax_code_id,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM sales_receipt_items WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE sales_receipt_items SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM sales_receipt_items WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Complaints:
    def __init__(self, id: int = None, customer_id: int = None, order_id: int = None, product_id: int = None, description: str = None, resolved: bool = None, created_at: str = None, resolved_at: str = None):
        self.id = id
        self.customer_id = customer_id
        self.order_id = order_id
        self.product_id = product_id
        self.description = description
        self.resolved = resolved
        self.created_at = created_at
        self.resolved_at = resolved_at

    @staticmethod
    def create(customer_id: int, order_id: int, product_id: int, description: str, resolved: bool, created_at: str, resolved_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO complaints (customer_id, order_id, product_id, description, resolved, created_at, resolved_at) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *", (customer_id, order_id, product_id, description, resolved, created_at, resolved_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM complaints WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE complaints SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM complaints WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Customers:
    def __init__(self, id: int = None, type: str = None, company_name: str = None, first_name: str = None, last_name: str = None, email: str = None, phone: str = None, address_line: str = None, postal_code: str = None, city: str = None, country: str = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.type = type
        self.company_name = company_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address_line = address_line
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(type: str, company_name: str, first_name: str, last_name: str, email: str, phone: str, address_line: str, postal_code: str, city: str, country: str, created_at: str, updated_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO customers (type, company_name, first_name, last_name, email, phone, address_line, postal_code, city, country, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *", (type, company_name, first_name, last_name, email, phone, address_line, postal_code, city, country, created_at, updated_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM customers WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE customers SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM customers WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Sales_receipts:
    def __init__(self, id: int = None, receipt_number: str = None, branch_id: int = None, pos_terminal_id: int = None, sale_datetime: str = None, customer_id: int = None, total_amount: float = None, payment_method_id: int = None, payment_reference: str = None):
        self.id = id
        self.receipt_number = receipt_number
        self.branch_id = branch_id
        self.pos_terminal_id = pos_terminal_id
        self.sale_datetime = sale_datetime
        self.customer_id = customer_id
        self.total_amount = total_amount
        self.payment_method_id = payment_method_id
        self.payment_reference = payment_reference

    @staticmethod
    def create(receipt_number: str, branch_id: int, pos_terminal_id: int, sale_datetime: str, customer_id: int, total_amount: float, payment_method_id: int, payment_reference: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO sales_receipts (receipt_number, branch_id, pos_terminal_id, sale_datetime, customer_id, total_amount, payment_method_id, payment_reference) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *", (receipt_number, branch_id, pos_terminal_id, sale_datetime, customer_id, total_amount, payment_method_id, payment_reference,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM sales_receipts WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE sales_receipts SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM sales_receipts WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Customer_feedback:
    def __init__(self, id: int = None, customer_id: int = None, branch_id: int = None, order_id: int = None, rating: int = None, comment: str = None, created_at: str = None):
        self.id = id
        self.customer_id = customer_id
        self.branch_id = branch_id
        self.order_id = order_id
        self.rating = rating
        self.comment = comment
        self.created_at = created_at

    @staticmethod
    def create(customer_id: int, branch_id: int, order_id: int, rating: int, comment: str, created_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO customer_feedback (customer_id, branch_id, order_id, rating, comment, created_at) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *", (customer_id, branch_id, order_id, rating, comment, created_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM customer_feedback WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE customer_feedback SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM customer_feedback WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Shift_schedule:
    def __init__(self, id: int = None, shift_id: int = None, employee_id: int = None, schedule_date: str = None, assigned_hours: float = None):
        self.id = id
        self.shift_id = shift_id
        self.employee_id = employee_id
        self.schedule_date = schedule_date
        self.assigned_hours = assigned_hours

    @staticmethod
    def create(shift_id: int, employee_id: int, schedule_date: str, assigned_hours: float) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO shift_schedule (shift_id, employee_id, schedule_date, assigned_hours) VALUES (%s, %s, %s, %s) RETURNING *", (shift_id, employee_id, schedule_date, assigned_hours,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM shift_schedule WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE shift_schedule SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM shift_schedule WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Production_feedback:
    def __init__(self, id: int = None, plan_item_id: int = None, user_id: int = None, produced_qty: float = None, timestamp: str = None):
        self.id = id
        self.plan_item_id = plan_item_id
        self.user_id = user_id
        self.produced_qty = produced_qty
        self.timestamp = timestamp

    @staticmethod
    def create(plan_item_id: int, user_id: int, produced_qty: float, timestamp: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO production_feedback (plan_item_id, user_id, produced_qty, timestamp) VALUES (%s, %s, %s, %s) RETURNING *", (plan_item_id, user_id, produced_qty, timestamp,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM production_feedback WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE production_feedback SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM production_feedback WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Shifts:
    def __init__(self, id: int = None, branch_id: int = None, name: str = None, start_time: str = None, end_time: str = None):
        self.id = id
        self.branch_id = branch_id
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    @staticmethod
    def create(branch_id: int, name: str, start_time: str, end_time: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO shifts (branch_id, name, start_time, end_time) VALUES (%s, %s, %s, %s) RETURNING *", (branch_id, name, start_time, end_time,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM shifts WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE shifts SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM shifts WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Supplier_order_items:
    def __init__(self, id: int = None, order_id: int = None, ingredient_id: int = None, qty: float = None, unit_price: float = None, received_amount: float = None, received: bool = None, received_at: str = None, tax_code_id: int = None):
        self.id = id
        self.order_id = order_id
        self.ingredient_id = ingredient_id
        self.qty = qty
        self.unit_price = unit_price
        self.received_amount = received_amount
        self.received = received
        self.received_at = received_at
        self.tax_code_id = tax_code_id

    @staticmethod
    def create(order_id: int, ingredient_id: int, qty: float, unit_price: float, received_amount: float, received: bool, received_at: str, tax_code_id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO supplier_order_items (order_id, ingredient_id, qty, unit_price, received_amount, received, received_at, tax_code_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING *", (order_id, ingredient_id, qty, unit_price, received_amount, received, received_at, tax_code_id,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM supplier_order_items WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE supplier_order_items SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM supplier_order_items WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Goods_receipt_items:
    def __init__(self, id: int = None, receipt_id: int = None, ingredient_id: int = None, qty: float = None, unit_price: float = None, tax_code_id: int = None):
        self.id = id
        self.receipt_id = receipt_id
        self.ingredient_id = ingredient_id
        self.qty = qty
        self.unit_price = unit_price
        self.tax_code_id = tax_code_id

    @staticmethod
    def create(receipt_id: int, ingredient_id: int, qty: float, unit_price: float, tax_code_id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO goods_receipt_items (receipt_id, ingredient_id, qty, unit_price, tax_code_id) VALUES (%s, %s, %s, %s, %s) RETURNING *", (receipt_id, ingredient_id, qty, unit_price, tax_code_id,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM goods_receipt_items WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE goods_receipt_items SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM goods_receipt_items WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Supplier_invoice_items:
    def __init__(self, id: int = None, invoice_id: int = None, ingredient_id: int = None, qty: float = None, unit_price: float = None, tax_code_id: int = None):
        self.id = id
        self.invoice_id = invoice_id
        self.ingredient_id = ingredient_id
        self.qty = qty
        self.unit_price = unit_price
        self.tax_code_id = tax_code_id

    @staticmethod
    def create(invoice_id: int, ingredient_id: int, qty: float, unit_price: float, tax_code_id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO supplier_invoice_items (invoice_id, ingredient_id, qty, unit_price, tax_code_id) VALUES (%s, %s, %s, %s, %s) RETURNING *", (invoice_id, ingredient_id, qty, unit_price, tax_code_id,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM supplier_invoice_items WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE supplier_invoice_items SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM supplier_invoice_items WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Refund_reasons:
    def __init__(self, id: int = None, code: str = None, description: str = None):
        self.id = id
        self.code = code
        self.description = description

    @staticmethod
    def create(code: str, description: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO refund_reasons (code, description) VALUES (%s, %s) RETURNING *", (code, description,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM refund_reasons WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE refund_reasons SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM refund_reasons WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Supplier_orders:
    def __init__(self, id: int = None, order_number: str = None, supplier_id: int = None, branch_id: int = None, order_date: str = None, status: str = None, expected_date: str = None, total_amount: float = None):
        self.id = id
        self.order_number = order_number
        self.supplier_id = supplier_id
        self.branch_id = branch_id
        self.order_date = order_date
        self.status = status
        self.expected_date = expected_date
        self.total_amount = total_amount

    @staticmethod
    def create(order_number: str, supplier_id: int, branch_id: int, order_date: str, status: str, expected_date: str, total_amount: float) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO supplier_orders (order_number, supplier_id, branch_id, order_date, status, expected_date, total_amount) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *", (order_number, supplier_id, branch_id, order_date, status, expected_date, total_amount,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM supplier_orders WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE supplier_orders SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM supplier_orders WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Pos_terminals:
    def __init__(self, id: int = None, branch_id: int = None, terminal_code: str = None, description: str = None, is_active: bool = None):
        self.id = id
        self.branch_id = branch_id
        self.terminal_code = terminal_code
        self.description = description
        self.is_active = is_active

    @staticmethod
    def create(branch_id: int, terminal_code: str, description: str, is_active: bool) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO pos_terminals (branch_id, terminal_code, description, is_active) VALUES (%s, %s, %s, %s) RETURNING *", (branch_id, terminal_code, description, is_active,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM pos_terminals WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE pos_terminals SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM pos_terminals WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Goods_receipts:
    def __init__(self, id: int = None, receipt_number: str = None, supplier_order_id: int = None, receipt_date: str = None, created_at: str = None):
        self.id = id
        self.receipt_number = receipt_number
        self.supplier_order_id = supplier_order_id
        self.receipt_date = receipt_date
        self.created_at = created_at

    @staticmethod
    def create(receipt_number: str, supplier_order_id: int, receipt_date: str, created_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO goods_receipts (receipt_number, supplier_order_id, receipt_date, created_at) VALUES (%s, %s, %s, %s) RETURNING *", (receipt_number, supplier_order_id, receipt_date, created_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM goods_receipts WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE goods_receipts SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM goods_receipts WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Supplier_invoices:
    def __init__(self, id: int = None, invoice_number: str = None, supplier_id: int = None, supplier_order_id: int = None, invoice_date: str = None, due_date: str = None, total_amount: float = None, payment_status: str = None):
        self.id = id
        self.invoice_number = invoice_number
        self.supplier_id = supplier_id
        self.supplier_order_id = supplier_order_id
        self.invoice_date = invoice_date
        self.due_date = due_date
        self.total_amount = total_amount
        self.payment_status = payment_status

    @staticmethod
    def create(invoice_number: str, supplier_id: int, supplier_order_id: int, invoice_date: str, due_date: str, total_amount: float, payment_status: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO supplier_invoices (invoice_number, supplier_id, supplier_order_id, invoice_date, due_date, total_amount, payment_status) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *", (invoice_number, supplier_id, supplier_order_id, invoice_date, due_date, total_amount, payment_status,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM supplier_invoices WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE supplier_invoices SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM supplier_invoices WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Payment_transactions:
    def __init__(self, id: int = None, account_id: int = None, payment_method_id: int = None, reference_type: str = None, reference_id: int = None, amount: float = None, currency: str = None, direction: str = None, transaction_date: str = None, created_at: str = None):
        self.id = id
        self.account_id = account_id
        self.payment_method_id = payment_method_id
        self.reference_type = reference_type
        self.reference_id = reference_id
        self.amount = amount
        self.currency = currency
        self.direction = direction
        self.transaction_date = transaction_date
        self.created_at = created_at

    @staticmethod
    def create(account_id: int, payment_method_id: int, reference_type: str, reference_id: int, amount: float, currency: str, direction: str, transaction_date: str, created_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO payment_transactions (account_id, payment_method_id, reference_type, reference_id, amount, currency, direction, transaction_date, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *", (account_id, payment_method_id, reference_type, reference_id, amount, currency, direction, transaction_date, created_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM payment_transactions WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE payment_transactions SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM payment_transactions WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Machines:
    def __init__(self, id: int = None, branch_id: int = None, name: str = None, serial_number: str = None, purchase_date: str = None, last_maintenance: str = None):
        self.id = id
        self.branch_id = branch_id
        self.name = name
        self.serial_number = serial_number
        self.purchase_date = purchase_date
        self.last_maintenance = last_maintenance

    @staticmethod
    def create(branch_id: int, name: str, serial_number: str, purchase_date: str, last_maintenance: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO machines (branch_id, name, serial_number, purchase_date, last_maintenance) VALUES (%s, %s, %s, %s, %s) RETURNING *", (branch_id, name, serial_number, purchase_date, last_maintenance,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM machines WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE machines SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM machines WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Branch_opening_hours:
    def __init__(self, id: int = None, branch_id: int = None, weekday: int = None, opens: str = None, closes: str = None):
        self.id = id
        self.branch_id = branch_id
        self.weekday = weekday
        self.opens = opens
        self.closes = closes

    @staticmethod
    def create(branch_id: int, weekday: int, opens: str, closes: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO branch_opening_hours (branch_id, weekday, opens, closes) VALUES (%s, %s, %s, %s) RETURNING *", (branch_id, weekday, opens, closes,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM branch_opening_hours WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE branch_opening_hours SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM branch_opening_hours WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Tax_codes:
    def __init__(self, id: int = None, name: str = None, rate: float = None, valid_from: str = None, valid_to: str = None):
        self.id = id
        self.name = name
        self.rate = rate
        self.valid_from = valid_from
        self.valid_to = valid_to

    @staticmethod
    def create(name: str, rate: float, valid_from: str, valid_to: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO tax_codes (name, rate, valid_from, valid_to) VALUES (%s, %s, %s, %s) RETURNING *", (name, rate, valid_from, valid_to,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM tax_codes WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE tax_codes SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM tax_codes WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Ingredients:
    def __init__(self, id: int = None, name: str = None, unit: str = None, purchase_price: float = None, tax_code_id: int = None, is_active: bool = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.name = name
        self.unit = unit
        self.purchase_price = purchase_price
        self.tax_code_id = tax_code_id
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(name: str, unit: str, purchase_price: float, tax_code_id: int, is_active: bool, created_at: str, updated_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO ingredients (name, unit, purchase_price, tax_code_id, is_active, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *", (name, unit, purchase_price, tax_code_id, is_active, created_at, updated_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM ingredients WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE ingredients SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM ingredients WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Recipe_items:
    def __init__(self, id: int = None, recipe_id: int = None, ingredient_id: int = None, quantity: float = None, unit: str = None):
        self.id = id
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.quantity = quantity
        self.unit = unit

    @staticmethod
    def create(recipe_id: int, ingredient_id: int, quantity: float, unit: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO recipe_items (recipe_id, ingredient_id, quantity, unit) VALUES (%s, %s, %s, %s) RETURNING *", (recipe_id, ingredient_id, quantity, unit,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM recipe_items WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE recipe_items SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM recipe_items WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Customer_orders:
    def __init__(self, id: int = None, order_number: str = None, customer_id: int = None, customer_name: str = None, branch_id: int = None, order_datetime: str = None, desired_datetime: str = None, serial: str = None, serial_end: str = None, status: str = None, total_amount: float = None, payment_status: str = None, comment: str = None):
        self.id = id
        self.order_number = order_number
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.branch_id = branch_id
        self.order_datetime = order_datetime
        self.desired_datetime = desired_datetime
        self.serial = serial
        self.serial_end = serial_end
        self.status = status
        self.total_amount = total_amount
        self.payment_status = payment_status
        self.comment = comment

    @staticmethod
    def create(order_number: str, customer_id: int, customer_name: str, branch_id: int, order_datetime: str, desired_datetime: str, serial: str, serial_end: str, status: str, total_amount: float, payment_status: str, comment: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO customer_orders (order_number, customer_id, customer_name, branch_id, order_datetime, desired_datetime, serial, serial_end, status, total_amount, payment_status, comment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *", (order_number, customer_id, customer_name, branch_id, order_datetime, desired_datetime, serial, serial_end, status, total_amount, payment_status, comment,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM customer_orders WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE customer_orders SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM customer_orders WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Production_plans:
    def __init__(self, id: int = None, branch_id: int = None, planned_date: str = None, status: str = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.branch_id = branch_id
        self.planned_date = planned_date
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    @staticmethod
    def create(branch_id: int, planned_date: str, status: str, created_at: str, updated_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO production_plans (branch_id, planned_date, status, created_at, updated_at) VALUES (%s, %s, %s, %s, %s) RETURNING *", (branch_id, planned_date, status, created_at, updated_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM production_plans WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE production_plans SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM production_plans WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Production_plan_items:
    def __init__(self, id: int = None, plan_id: int = None, product_id: int = None, planned_qty: float = None, produced_qty: float = None):
        self.id = id
        self.plan_id = plan_id
        self.product_id = product_id
        self.planned_qty = planned_qty
        self.produced_qty = produced_qty

    @staticmethod
    def create(plan_id: int, product_id: int, planned_qty: float, produced_qty: float) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO production_plan_items (plan_id, product_id, planned_qty, produced_qty) VALUES (%s, %s, %s, %s) RETURNING *", (plan_id, product_id, planned_qty, produced_qty,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM production_plan_items WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE production_plan_items SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM production_plan_items WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Refunds:
    def __init__(self, id: int = None, receipt_id: int = None, order_id: int = None, refund_datetime: str = None, total_refund_amount: float = None, payment_method_id: int = None, account_id: int = None, reason_id: int = None, created_by: int = None, note: str = None, created_at: str = None):
        self.id = id
        self.receipt_id = receipt_id
        self.order_id = order_id
        self.refund_datetime = refund_datetime
        self.total_refund_amount = total_refund_amount
        self.payment_method_id = payment_method_id
        self.account_id = account_id
        self.reason_id = reason_id
        self.created_by = created_by
        self.note = note
        self.created_at = created_at

    @staticmethod
    def create(receipt_id: int, order_id: int, refund_datetime: str, total_refund_amount: float, payment_method_id: int, account_id: int, reason_id: int, created_by: int, note: str, created_at: str) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO refunds (receipt_id, order_id, refund_datetime, total_refund_amount, payment_method_id, account_id, reason_id, created_by, note, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *", (receipt_id, order_id, refund_datetime, total_refund_amount, payment_method_id, account_id, reason_id, created_by, note, created_at,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM refunds WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE refunds SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM refunds WHERE id = %s", (id,))
            conn.commit()
        conn.close()


class Refund_items:
    def __init__(self, id: int = None, refund_id: int = None, product_id: int = None, qty: float = None, unit_price: float = None, tax_code_id: int = None):
        self.id = id
        self.refund_id = refund_id
        self.product_id = product_id
        self.qty = qty
        self.unit_price = unit_price
        self.tax_code_id = tax_code_id

    @staticmethod
    def create(refund_id: int, product_id: int, qty: float, unit_price: float, tax_code_id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("INSERT INTO refund_items (refund_id, product_id, qty, unit_price, tax_code_id) VALUES (%s, %s, %s, %s, %s) RETURNING *", (refund_id, product_id, qty, unit_price, tax_code_id,))
            result = cur.fetchone()
            conn.commit()
        conn.close()
        return result

    @staticmethod
    def read(id: int) -> tuple | None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM refund_items WHERE id = %s", (id,))
            row = cur.fetchone()
        conn.close()
        return row

    @staticmethod
    def update(id: int, **kwargs) -> None:
        conn = connect()
        set_clause = ', '.join([f"{k} = %s" for k in kwargs.keys()])
        values = list(kwargs.values()) + [id]
        with conn.cursor() as cur:
            cur.execute(f"UPDATE refund_items SET {set_clause} WHERE id = %s", values)
            conn.commit()
        conn.close()

    @staticmethod
    def delete(id: int) -> None:
        conn = connect()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM refund_items WHERE id = %s", (id,))
            conn.commit()
        conn.close()
