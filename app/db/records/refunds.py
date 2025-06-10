class Refunds:
    table_name = "refunds"

    def __init__(self, id: int = None, receipt_id: int = None, order_id: int = None, refund_datetime: str = None, total_refund_amount: float = None, payment_method_id: int = None, account_id: int = None, reason_id: int = None, created_by: int = None, note: str = None, created_at: str = None):
        self.id = id
        self.receipt_id = receipt_id
        self.order_id = order_id
        self.refund_datetime = refund_datetime
        self.total_refund_amount = total_refund_amount
        self.payment_method_id = payment_method_id
        self.account_id = account_id
        self.reason_id = reason_id
        self.created_by = created_by
        self.note = note
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id, "receipt_id": self.receipt_id, "order_id": self.order_id, "refund_datetime": self.refund_datetime, "total_refund_amount": self.total_refund_amount, "payment_method_id": self.payment_method_id, "account_id": self.account_id, "reason_id": self.reason_id, "created_by": self.created_by, "note": self.note, "created_at": self.created_at
        }
