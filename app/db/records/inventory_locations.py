class Inventory_locations:
    table_name = "inventory_locations"

    def __init__(self, id: int = None, warehouse_id: int = None, code: str = None, description: str = None):
        self.id = id
        self.warehouse_id = warehouse_id
        self.code = code
        self.description = description

    def to_dict(self):
        return {
            "id": self.id, "warehouse_id": self.warehouse_id, "code": self.code, "description": self.description
        }
