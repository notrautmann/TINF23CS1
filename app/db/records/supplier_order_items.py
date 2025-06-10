class Supplier_order_items:
    table_name = "supplier_order_items"

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

    def to_dict(self):
        return {
            "id": self.id, "order_id": self.order_id, "ingredient_id": self.ingredient_id, "qty": self.qty, "unit_price": self.unit_price, "received_amount": self.received_amount, "received": self.received, "received_at": self.received_at, "tax_code_id": self.tax_code_id
        }
