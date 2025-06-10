class Users:
    table_name = "users"

    def __init__(self, id: int = None, username: str = None, password_hash: str = None, role_id: int = None, employee_id: int = None, is_active: bool = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.username = username
        self.password_hash = password_hash
        self.role_id = role_id
        self.employee_id = employee_id
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id, "username": self.username, "password_hash": self.password_hash, "role_id": self.role_id, "employee_id": self.employee_id, "is_active": self.is_active, "created_at": self.created_at, "updated_at": self.updated_at
        }
