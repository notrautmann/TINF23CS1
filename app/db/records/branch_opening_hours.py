class Branch_opening_hours:
    table_name = "branch_opening_hours"

    def __init__(self, id: int = None, branch_id: int = None, weekday: int = None, opens: str = None, closes: str = None):
        self.id = id
        self.branch_id = branch_id
        self.weekday = weekday
        self.opens = opens
        self.closes = closes

    def to_dict(self):
        return {
            "id": self.id, "branch_id": self.branch_id, "weekday": self.weekday, "opens": self.opens, "closes": self.closes
        }
