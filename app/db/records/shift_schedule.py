class Shift_schedule:
    table_name = "shift_schedule"

    def __init__(self, id: int = None, shift_id: int = None, employee_id: int = None, schedule_date: str = None, assigned_hours: float = None):
        self.id = id
        self.shift_id = shift_id
        self.employee_id = employee_id
        self.schedule_date = schedule_date
        self.assigned_hours = assigned_hours

    def to_dict(self):
        return {
            "id": self.id, "shift_id": self.shift_id, "employee_id": self.employee_id, "schedule_date": self.schedule_date, "assigned_hours": self.assigned_hours
        }
