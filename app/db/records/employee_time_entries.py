class Employee_time_entries:
    table_name = "employee_time_entries"

    def __init__(self, id: int = None, employee_id: int = None, branch_id: int = None, clock_in: str = None, clock_out: str = None, break_minutes: int = None):
        self.id = id
        self.employee_id = employee_id
        self.branch_id = branch_id
        self.clock_in = clock_in
        self.clock_out = clock_out
        self.break_minutes = break_minutes

    def to_dict(self):
        return {
            "id": self.id, "employee_id": self.employee_id, "branch_id": self.branch_id, "clock_in": self.clock_in, "clock_out": self.clock_out, "break_minutes": self.break_minutes
        }
