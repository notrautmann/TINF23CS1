class Warehouses:
    table_name = "warehouses"

    def __init__(self, id: int = None, branch_id: int = None, name: str = None, description: str = None):
        self.id = id
        self.branch_id = branch_id
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            "id": self.id, "branch_id": self.branch_id, "name": self.name, "description": self.description
        }
