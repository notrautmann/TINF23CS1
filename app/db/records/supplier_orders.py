class Supplier_orders:
    table_name = "supplier_orders"

    def __init__(self, id: int = None, order_number: str = None, supplier_id: int = None, branch_id: int = None, order_date: str = None, status: str = None, expected_date: str = None, total_amount: float = None):
        self.id = id
        self.order_number = order_number
        self.supplier_id = supplier_id
        self.branch_id = branch_id
        self.order_date = order_date
        self.status = status
        self.expected_date = expected_date
        self.total_amount = total_amount

    def to_dict(self):
        return {
            "id": self.id, "order_number": self.order_number, "supplier_id": self.supplier_id, "branch_id": self.branch_id, "order_date": self.order_date, "status": self.status, "expected_date": self.expected_date, "total_amount": self.total_amount
        }
