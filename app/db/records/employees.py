class Employees:
    table_name = "employees"

    def __init__(self, id: int = None, first_name: str = None, last_name: str = None, email: str = None, phone: str = None, hire_date: str = None, termination_date: str = None, hourly_wage: float = None, monthly_salary: float = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.hire_date = hire_date
        self.termination_date = termination_date
        self.hourly_wage = hourly_wage
        self.monthly_salary = monthly_salary
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id, "first_name": self.first_name, "last_name": self.last_name, "email": self.email, "phone": self.phone, "hire_date": self.hire_date, "termination_date": self.termination_date, "hourly_wage": self.hourly_wage, "monthly_salary": self.monthly_salary, "created_at": self.created_at, "updated_at": self.updated_at
        }
