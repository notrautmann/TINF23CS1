class Goods_receipts:
    table_name = "goods_receipts"

    def __init__(self, id: int = None, receipt_number: str = None, supplier_order_id: int = None, receipt_date: str = None, created_at: str = None):
        self.id = id
        self.receipt_number = receipt_number
        self.supplier_order_id = supplier_order_id
        self.receipt_date = receipt_date
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id, "receipt_number": self.receipt_number, "supplier_order_id": self.supplier_order_id, "receipt_date": self.receipt_date, "created_at": self.created_at
        }
