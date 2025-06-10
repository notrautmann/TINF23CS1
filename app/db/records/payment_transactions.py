class Payment_transactions:
    table_name = "payment_transactions"

    def __init__(self, id: int = None, account_id: int = None, payment_method_id: int = None, reference_type: str = None, reference_id: int = None, amount: float = None, currency: str = None, direction: str = None, transaction_date: str = None, created_at: str = None):
        self.id = id
        self.account_id = account_id
        self.payment_method_id = payment_method_id
        self.reference_type = reference_type
        self.reference_id = reference_id
        self.amount = amount
        self.currency = currency
        self.direction = direction
        self.transaction_date = transaction_date
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id, "account_id": self.account_id, "payment_method_id": self.payment_method_id, "reference_type": self.reference_type, "reference_id": self.reference_id, "amount": self.amount, "currency": self.currency, "direction": self.direction, "transaction_date": self.transaction_date, "created_at": self.created_at
        }
