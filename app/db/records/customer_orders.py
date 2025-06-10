class Customer_orders:
    table_name = "customer_orders"

    def __init__(self, id: int = None, order_number: str = None, customer_id: int = None, customer_name: str = None, branch_id: int = None, order_datetime: str = None, desired_datetime: str = None, serial: str = None, serial_end: str = None, status: str = None, total_amount: float = None, payment_status: str = None, comment: str = None):
        self.id = id
        self.order_number = order_number
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.branch_id = branch_id
        self.order_datetime = order_datetime
        self.desired_datetime = desired_datetime
        self.serial = serial
        self.serial_end = serial_end
        self.status = status
        self.total_amount = total_amount
        self.payment_status = payment_status
        self.comment = comment

    def to_dict(self):
        return {
            "id": self.id, "order_number": self.order_number, "customer_id": self.customer_id, "customer_name": self.customer_name, "branch_id": self.branch_id, "order_datetime": self.order_datetime, "desired_datetime": self.desired_datetime, "serial": self.serial, "serial_end": self.serial_end, "status": self.status, "total_amount": self.total_amount, "payment_status": self.payment_status, "comment": self.comment
        }
