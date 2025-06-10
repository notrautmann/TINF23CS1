class Production_feedback:
    table_name = "production_feedback"

    def __init__(self, id: int = None, plan_item_id: int = None, user_id: int = None, produced_qty: float = None, timestamp: str = None):
        self.id = id
        self.plan_item_id = plan_item_id
        self.user_id = user_id
        self.produced_qty = produced_qty
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "id": self.id, "plan_item_id": self.plan_item_id, "user_id": self.user_id, "produced_qty": self.produced_qty, "timestamp": self.timestamp
        }
