class Accounts:
    table_name = "accounts"

    def __init__(self, id: int = None, name: str = None, account_number: str = None, iban: str = None, bic: str = None, description: str = None):
        self.id = id
        self.name = name
        self.account_number = account_number
        self.iban = iban
        self.bic = bic
        self.description = description

    def to_dict(self):
        return {
            "id": self.id, "name": self.name, "account_number": self.account_number, "iban": self.iban, "bic": self.bic, "description": self.description
        }
