class Tax_codes:
    table_name = "tax_codes"

    def __init__(self, id: int = None, name: str = None, rate: float = None, valid_from: str = None, valid_to: str = None):
        self.id = id
        self.name = name
        self.rate = rate
        self.valid_from = valid_from
        self.valid_to = valid_to

    def to_dict(self):
        return {
            "id": self.id, "name": self.name, "rate": self.rate, "valid_from": self.valid_from, "valid_to": self.valid_to
        }
