class Supplier_products:
    table_name = "supplier_products"

    def __init__(self, id: int = None, supplier_id: int = None, ingredient_id: int = None, supplier_sku: str = None, purchase_price: float = None, min_order_qty: float = None, lead_time_days: int = None):
        self.id = id
        self.supplier_id = supplier_id
        self.ingredient_id = ingredient_id
        self.supplier_sku = supplier_sku
        self.purchase_price = purchase_price
        self.min_order_qty = min_order_qty
        self.lead_time_days = lead_time_days

    def to_dict(self):
        return {
            "id": self.id, "supplier_id": self.supplier_id, "ingredient_id": self.ingredient_id, "supplier_sku": self.supplier_sku, "purchase_price": self.purchase_price, "min_order_qty": self.min_order_qty, "lead_time_days": self.lead_time_days
        }
