class Refund_reasons:
    table_name = "refund_reasons"

    def __init__(self, id: int = None, code: str = None, description: str = None):
        self.id = id
        self.code = code
        self.description = description

    def to_dict(self):
        return {
            "id": self.id, "code": self.code, "description": self.description
        }
