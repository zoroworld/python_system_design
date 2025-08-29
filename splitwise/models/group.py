# models/group.py
from models.user import User

class Group:
    """Represents a group of users"""
    def __init__(self, name: str, created_by: User):
        self.name = name
        self.created_by = created_by
        self.members = []

    def add_member(self, user: User):
        self.members.append(user)

    def __repr__(self):
        return f"Group({self.name}, Members: {[m.name for m in self.members]})"
