class Recipe_items:
    table_name = "recipe_items"

    def __init__(self, id: int = None, recipe_id: int = None, ingredient_id: int = None, quantity: float = None, unit: str = None):
        self.id = id
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.quantity = quantity
        self.unit = unit

    def to_dict(self):
        return {
            "id": self.id, "recipe_id": self.recipe_id, "ingredient_id": self.ingredient_id, "quantity": self.quantity, "unit": self.unit
        }
