class Pos_terminals:
    table_name = "pos_terminals"

    def __init__(self, id: int = None, branch_id: int = None, terminal_code: str = None, description: str = None, is_active: bool = None):
        self.id = id
        self.branch_id = branch_id
        self.terminal_code = terminal_code
        self.description = description
        self.is_active = is_active

    def to_dict(self):
        return {
            "id": self.id, "branch_id": self.branch_id, "terminal_code": self.terminal_code, "description": self.description, "is_active": self.is_active
        }
