class Production_plans:
    table_name = "production_plans"

    def __init__(self, id: int = None, branch_id: int = None, planned_date: str = None, status: str = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.branch_id = branch_id
        self.planned_date = planned_date
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id, "branch_id": self.branch_id, "planned_date": self.planned_date, "status": self.status, "created_at": self.created_at, "updated_at": self.updated_at
        }
