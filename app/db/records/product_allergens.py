class Product_allergens:
    table_name = "product_allergens"

    def __init__(self, product_id: int = None, allergen_id: int = None):
        self.product_id = product_id
        self.allergen_id = allergen_id

    def to_dict(self):
        return {
            "product_id": self.product_id, "allergen_id": self.allergen_id
        }
