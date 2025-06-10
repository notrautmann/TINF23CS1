class Machines:
    table_name = "machines"

    def __init__(self, id: int = None, branch_id: int = None, name: str = None, serial_number: str = None, purchase_date: str = None, last_maintenance: str = None):
        self.id = id
        self.branch_id = branch_id
        self.name = name
        self.serial_number = serial_number
        self.purchase_date = purchase_date
        self.last_maintenance = last_maintenance

    def to_dict(self):
        return {
            "id": self.id, "branch_id": self.branch_id, "name": self.name, "serial_number": self.serial_number, "purchase_date": self.purchase_date, "last_maintenance": self.last_maintenance
        }
