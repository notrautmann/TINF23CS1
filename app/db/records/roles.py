class Roles:
    table_name = "roles"

    def __init__(self, id: int = None, name: str = None, description: str = None):
        self.id = id
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            "id": self.id, "name": self.name, "description": self.description
        }
