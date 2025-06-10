class Customer_feedback:
    table_name = "customer_feedback"

    def __init__(self, id: int = None, customer_id: int = None, branch_id: int = None, order_id: int = None, rating: int = None, comment: str = None, created_at: str = None):
        self.id = id
        self.customer_id = customer_id
        self.branch_id = branch_id
        self.order_id = order_id
        self.rating = rating
        self.comment = comment
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": self.id, "customer_id": self.customer_id, "branch_id": self.branch_id, "order_id": self.order_id, "rating": self.rating, "comment": self.comment, "created_at": self.created_at
        }
