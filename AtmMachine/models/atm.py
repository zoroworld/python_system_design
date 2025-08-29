# models/atm.py
from models.user import User
from abc import ABC, abstractmethod

class Atm:
    atm_users = {}   # shared across all instances

    def __init__(self, user: User, amount, pin):
        self.user = user
        self.amount = amount
        self.pin = pin
        Atm.atm_users[user.name] = {"amount": amount, "pin": pin, "user": user}

    @classmethod
    def get_all_user(cls):
        return cls.atm_users


# ---- Withdraw ----
class Withdraw(ABC):
    def __init__(self, atm):
        self.atm = atm

    @abstractmethod
    def withdraw_amount(self, amount):
        pass


class QuickWithdraw(Withdraw):

    def withdraw_amount(self, amount):
        if Atm.atm_users[self.atm.user.name]["amount"] >= amount:
            Atm.atm_users[self.atm.user.name]["amount"] -= amount
            print(f"Withdrawn {amount}. Balance: {Atm.atm_users[self.atm.user.name]['amount']}")
        else:
            print("Insufficient Balance")


# ---- Deposit ----
class Deposit(ABC):
    def __init__(self, atm):
        self.atm = atm

    @abstractmethod
    def add_amount(self, amount):
        pass


class QuickDeposit(Deposit):
    def add_amount(self, amount):
        Atm.atm_users[self.atm.user.name]["amount"] += amount
        print(f"Deposited {amount}. Balance: {Atm.atm_users[self.atm.user.name]['amount']}")


