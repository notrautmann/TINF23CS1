class Customer_order_items:
    table_name = "customer_order_items"

    def __init__(self, id: int = None, order_id: int = None, product_id: int = None, quantity: int = None, unit_price: float = None, tax_code_id: int = None):
        self.id = id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price
        self.tax_code_id = tax_code_id

    def to_dict(self):
        return {
            "id": self.id, "order_id": self.order_id, "product_id": self.product_id, "quantity": self.quantity, "unit_price": self.unit_price, "tax_code_id": self.tax_code_id
        }
