# models/atm_machine.py
from .atm import Atm, QuickWithdraw, QuickDeposit
from .user import User

class AtmMachine:
    def __init__(self):
        self.atm_user = {}
        self.get_store_atm()

    def get_store_atm(self):
        self.atm_user = Atm.get_all_user()

    def check_pin(self, pin: str):
        for user, data in self.atm_user.items():
            if str(data["pin"]) == pin:
                return data
        return None

    def display_user_account(self, user: User):
        print(f"Name {user.name} and amount is '{Atm.atm_users[user.name]['amount']}rs'")

    def start_atm(self):
        print("ATM machine started" + "--" * 30)

        count = 3
        data = None
        while count:
            pin = input("Enter the pin: ")
            data = self.check_pin(pin)
            if data:
                break
            print("Invalid PIN")
            count -= 1

        if not data:
            print("Please Enter after 24 hours")
            return

        user = data["user"]
        v_amount = data["amount"]
        v_pin = data["pin"]

        atm = Atm(user, v_amount,  v_pin)

        print('###' * 20)
        print(f"Hello {user.name}, Welcome!")
        print('###' * 20)

        while True:
            print("""
               1. Display Amount
               2. Withdraw Amount
               3. Deposit Amount
               4. Exit
               """)

            choose = int(input("Enter Your Choice: "))

            if choose == 1:
                self.display_user_account(user)

            elif choose == 2:
                amt = int(input("Enter the amount to withdraw: "))
                getqick_withdraw = QuickWithdraw(atm)
                getqick_withdraw.withdraw_amount(amt)

            elif choose == 3:
                amt = int(input("Enter the amount to deposit: "))
                getquick_deposit = QuickDeposit(atm)
                getquick_deposit.add_amount(amt)

            elif choose == 4:
                print("Thank you for using ATM")
                break
            else:
                print("Invalid choice")
