# models/user.py
class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"User({self.name})"
