class Supplier_invoices:
    table_name = "supplier_invoices"

    def __init__(self, id: int = None, invoice_number: str = None, supplier_id: int = None, supplier_order_id: int = None, invoice_date: str = None, due_date: str = None, total_amount: float = None, payment_status: str = None):
        self.id = id
        self.invoice_number = invoice_number
        self.supplier_id = supplier_id
        self.supplier_order_id = supplier_order_id
        self.invoice_date = invoice_date
        self.due_date = due_date
        self.total_amount = total_amount
        self.payment_status = payment_status

    def to_dict(self):
        return {
            "id": self.id, "invoice_number": self.invoice_number, "supplier_id": self.supplier_id, "supplier_order_id": self.supplier_order_id, "invoice_date": self.invoice_date, "due_date": self.due_date, "total_amount": self.total_amount, "payment_status": self.payment_status
        }
