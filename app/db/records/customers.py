class Customers:
    table_name = "customers"

    def __init__(self, id: int = None, type: str = None, company_name: str = None, first_name: str = None, last_name: str = None, email: str = None, phone: str = None, address_line: str = None, postal_code: str = None, city: str = None, country: str = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.type = type
        self.company_name = company_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address_line = address_line
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id, "type": self.type, "company_name": self.company_name, "first_name": self.first_name, "last_name": self.last_name, "email": self.email, "phone": self.phone, "address_line": self.address_line, "postal_code": self.postal_code, "city": self.city, "country": self.country, "created_at": self.created_at, "updated_at": self.updated_at
        }
