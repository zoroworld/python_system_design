# models/expense.py
from models.user import User
from datetime import datetime

class Expense:
    """Represents a single expense paid by someone"""
    def __init__(self, paid_by: User, amount: float, description: str, created_by: User):
        self.paid_by = paid_by
        self.amount = amount
        self.description = description
        self.created_by = created_by
        self.created_at = datetime.now()

    def __repr__(self):
        return f"Expense({self.description}, {self.amount}, paid by {self.paid_by.name})"


class ExpenseSplit:
    """Represents how an expense is split among users"""
    def __init__(self, expense: Expense, user: User, amount: float):
        self.expense = expense
        self.user = user
        self.amount = amount

    def __repr__(self):
        return f"{self.user.name} owes {self.expense.paid_by.name}: {self.amount}"
