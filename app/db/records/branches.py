class Branches:
    table_name = "branches"

    def __init__(self, id: int = None, name: str = None, address_line: str = None, postal_code: str = None, city: str = None, country: str = None, phone: str = None, email: str = None, opening_note: str = None, created_at: str = None, updated_at: str = None):
        self.id = id
        self.name = name
        self.address_line = address_line
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.phone = phone
        self.email = email
        self.opening_note = opening_note
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id, "name": self.name, "address_line": self.address_line, "postal_code": self.postal_code, "city": self.city, "country": self.country, "phone": self.phone, "email": self.email, "opening_note": self.opening_note, "created_at": self.created_at, "updated_at": self.updated_at
        }
