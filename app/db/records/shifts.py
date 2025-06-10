class Shifts:
    table_name = "shifts"

    def __init__(self, id: int = None, branch_id: int = None, name: str = None, start_time: str = None, end_time: str = None):
        self.id = id
        self.branch_id = branch_id
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self):
        return {
            "id": self.id, "branch_id": self.branch_id, "name": self.name, "start_time": self.start_time, "end_time": self.end_time
        }
