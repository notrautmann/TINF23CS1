class Complaints:
    table_name = "complaints"

    def __init__(self, id: int = None, customer_id: int = None, order_id: int = None, product_id: int = None, description: str = None, resolved: bool = None, created_at: str = None, resolved_at: str = None):
        self.id = id
        self.customer_id = customer_id
        self.order_id = order_id
        self.product_id = product_id
        self.description = description
        self.resolved = resolved
        self.created_at = created_at
        self.resolved_at = resolved_at

    def to_dict(self):
        return {
            "id": self.id, "customer_id": self.customer_id, "order_id": self.order_id, "product_id": self.product_id, "description": self.description, "resolved": self.resolved, "created_at": self.created_at, "resolved_at": self.resolved_at
        }
