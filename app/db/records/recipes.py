class Recipes:
    table_name = "recipes"

    def __init__(self, id: int = None, name: str = None, description: str = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id, "name": self.name, "description": self.description, "created_at": self.created_at, "updated_at": self.updated_at
        }
