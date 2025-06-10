class Ingredients:
    table_name = "ingredients"

    def __init__(self, id: int = None, name: str = None, unit: str = None, purchase_price: float = None, tax_code_id: int = None, is_active: bool = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.name = name
        self.unit = unit
        self.purchase_price = purchase_price
        self.tax_code_id = tax_code_id
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id, "name": self.name, "unit": self.unit, "purchase_price": self.purchase_price, "tax_code_id": self.tax_code_id, "is_active": self.is_active, "created_at": self.created_at, "updated_at": self.updated_at
        }
