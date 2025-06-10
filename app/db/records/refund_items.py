class Refund_items:
    table_name = "refund_items"

    def __init__(self, id: int = None, refund_id: int = None, product_id: int = None, qty: float = None, unit_price: float = None, tax_code_id: int = None):
        self.id = id
        self.refund_id = refund_id
        self.product_id = product_id
        self.qty = qty
        self.unit_price = unit_price
        self.tax_code_id = tax_code_id

    def to_dict(self):
        return {
            "id": self.id, "refund_id": self.refund_id, "product_id": self.product_id, "qty": self.qty, "unit_price": self.unit_price, "tax_code_id": self.tax_code_id
        }
