class Inventory_movements:
    table_name = "inventory_movements"

    def __init__(self, id: int = None, movement_type: str = None, ingredient_id: int = None, qty: float = None, unit: str = None, from_location_id: int = None, to_location_id: int = None, reference_type: str = None, reference_id: int = None, created_at: str = None, user_id: int = None):
        self.id = id
        self.movement_type = movement_type
        self.ingredient_id = ingredient_id
        self.qty = qty
        self.unit = unit
        self.from_location_id = from_location_id
        self.to_location_id = to_location_id
        self.reference_type = reference_type
        self.reference_id = reference_id
        self.created_at = created_at
        self.user_id = user_id

    def to_dict(self):
        return {
            "id": self.id, "movement_type": self.movement_type, "ingredient_id": self.ingredient_id, "qty": self.qty, "unit": self.unit, "from_location_id": self.from_location_id, "to_location_id": self.to_location_id, "reference_type": self.reference_type, "reference_id": self.reference_id, "created_at": self.created_at, "user_id": self.user_id
        }
