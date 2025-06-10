class Production_plan_items:
    table_name = "production_plan_items"

    def __init__(self, id: int = None, plan_id: int = None, product_id: int = None, planned_qty: float = None, produced_qty: float = None):
        self.id = id
        self.plan_id = plan_id
        self.product_id = product_id
        self.planned_qty = planned_qty
        self.produced_qty = produced_qty

    def to_dict(self):
        return {
            "id": self.id, "plan_id": self.plan_id, "product_id": self.product_id, "planned_qty": self.planned_qty, "produced_qty": self.produced_qty
        }
