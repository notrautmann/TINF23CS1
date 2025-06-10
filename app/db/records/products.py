class Products:
    table_name = "products"

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

    def to_dict(self):
        return {
            "id": self.id, "name": self.name, "sku": self.sku, "recipe_id": self.recipe_id, "sales_price": self.sales_price, "tax_code_id": self.tax_code_id, "is_active": self.is_active, "created_at": self.created_at, "updated_at": self.updated_at
        }
