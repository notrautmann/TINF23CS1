class Allergens:
    table_name = "allergens"

    def __init__(self, id: int = None, code: str = None, name: str = None, description: str = None):
        self.id = id
        self.code = code
        self.name = name
        self.description = description

    def to_dict(self):
        return {
            "id": self.id, "code": self.code, "name": self.name, "description": self.description
        }
