class Sales_receipts:
    table_name = "sales_receipts"

    def __init__(self, id: int = None, receipt_number: str = None, branch_id: int = None, pos_terminal_id: int = None, sale_datetime: str = None, customer_id: int = None, total_amount: float = None, payment_method_id: int = None, payment_reference: str = None):
        self.id = id
        self.receipt_number = receipt_number
        self.branch_id = branch_id
        self.pos_terminal_id = pos_terminal_id
        self.sale_datetime = sale_datetime
        self.customer_id = customer_id
        self.total_amount = total_amount
        self.payment_method_id = payment_method_id
        self.payment_reference = payment_reference

    def to_dict(self):
        return {
            "id": self.id, "receipt_number": self.receipt_number, "branch_id": self.branch_id, "pos_terminal_id": self.pos_terminal_id, "sale_datetime": self.sale_datetime, "customer_id": self.customer_id, "total_amount": self.total_amount, "payment_method_id": self.payment_method_id, "payment_reference": self.payment_reference
        }
