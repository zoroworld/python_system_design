# split_app.py
from models.user import User
from models.group import Group
from models.expense import Expense
from models.account import Account

class SplitApp:
    def startapp(self):
        # Create users
        A = User("Sumit", "8956123456")
        B = User("Amit", "9562358963")
        C = User("Rahul", "6589635489")
        D = User("Mikha", "7896524568")

        # Create a group
        group1 = Group("Hotel Trip", A)
        group1.add_member(A)
        group1.add_member(B)
        group1.add_member(C)
        group1.add_member(D)

        print(group1)

        # Add an expense
        expense1 = Expense(A, 4000, "Hotel", A)

        # Split equally
        n = len(group1.members)
        split_amount = expense1.amount // n

        accounts = []
        for member in group1.members:
            if member != expense1.paid_by:
                accounts.append(Account(member, expense1.paid_by, split_amount))

        # Interactive loop
        while True:
            print("\n--- Current Accounts ---")
            for idx, acc in enumerate(accounts):
                print(f"{idx+1}. {acc}")

            # check if all settled
            if all(acc.amount == 0 for acc in accounts):
                print("\n🎉 All accounts are settled! 🎉")
                break

            choice = input("\nEnter account number to settle (or 'q' to quit): ")
            if choice.lower() == 'q':
                print("Exiting settlement loop.")
                break

            try:
                idx = int(choice) - 1
                if idx < 0 or idx >= len(accounts):
                    print("Invalid choice. Try again.")
                    continue

                amount = float(input(f"Enter amount {accounts[idx].user.name} wants to pay {accounts[idx].owed_to.name}: "))
                accounts[idx].settle(amount)

            except ValueError:
                print("Invalid input. Please enter numbers only.")

