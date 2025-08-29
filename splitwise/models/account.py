# models/account.py
from models.user import User

class Account:
    """Tracks how much one user owes another"""
    def __init__(self, user: User, owed_to: User, amount: float):
        self.user = user
        self.owed_to = owed_to
        self.amount = amount

    def settle(self, payment: float):
        """Reduce the amount owed by a payment"""
        if payment >= self.amount:
            print(f"{self.user.name} fully settled with {self.owed_to.name}")
            self.amount = 0
        else:
            self.amount -= payment
            print(f"{self.user.name} partially settled with {self.owed_to.name}, Remaining: {self.amount}")

    def __repr__(self):
        return f"{self.user.name} owes {self.owed_to.name}: {self.amount}"
