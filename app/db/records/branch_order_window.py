class Branch_order_window:
    table_name = "branch_order_window"

    def __init__(self, id: int = None, branch_id: int = None, weekday: int = None, order_start: str = None, order_end: str = None):
        self.id = id
        self.branch_id = branch_id
        self.weekday = weekday
        self.order_start = order_start
        self.order_end = order_end

    def to_dict(self):
        return {
            "id": self.id, "branch_id": self.branch_id, "weekday": self.weekday, "order_start": self.order_start, "order_end": self.order_end
        }
