class Payment_methods:
    table_name = "payment_methods"

    def __init__(self, id: int = None, name: str = None, external_code: str = None, is_cash: bool = None):
        self.id = id
        self.name = name
        self.external_code = external_code
        self.is_cash = is_cash

    def to_dict(self):
        return {
            "id": self.id, "name": self.name, "external_code": self.external_code, "is_cash": self.is_cash
        }
