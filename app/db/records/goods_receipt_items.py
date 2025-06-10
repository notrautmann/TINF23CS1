class Goods_receipt_items:
    table_name = "goods_receipt_items"

    def __init__(self, id: int = None, receipt_id: int = None, ingredient_id: int = None, qty: float = None, unit_price: float = None, tax_code_id: int = None):
        self.id = id
        self.receipt_id = receipt_id
        self.ingredient_id = ingredient_id
        self.qty = qty
        self.unit_price = unit_price
        self.tax_code_id = tax_code_id

    def to_dict(self):
        return {
            "id": self.id, "receipt_id": self.receipt_id, "ingredient_id": self.ingredient_id, "qty": self.qty, "unit_price": self.unit_price, "tax_code_id": self.tax_code_id
        }
