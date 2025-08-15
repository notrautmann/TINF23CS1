class Ingredient_allergens:
    table_name = "ingredient_allergens"

    def __init__(self, ingredient_id: int = None, allergen_id: int = None):
        self.ingredient_id = ingredient_id
        self.allergen_id = allergen_id

    def to_dict(self):
        return {
            "ingredient_id": self.ingredient_id, "allergen_id": self.allergen_id
        }
