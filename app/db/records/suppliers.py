class Suppliers:
    table_name = "suppliers"

    def __init__(self, id: int = None, name: str = None, contact_name: str = None, email: str = None, phone: str = None, address_line: str = None, postal_code: str = None, city: str = None, country: str = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.name = name
        self.contact_name = contact_name
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
            "id": self.id, "name": self.name, "contact_name": self.contact_name, "email": self.email, "phone": self.phone, "address_line": self.address_line, "postal_code": self.postal_code, "city": self.city, "country": self.country, "created_at": self.created_at, "updated_at": self.updated_at
        }
