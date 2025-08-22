from models.notifier import Notifier
from models.subscriber import Subscriber

def main():
    notifier = Notifier()

    while True:
        print("\n--- NotifyMe App (Observer Pattern) ---")
        print("1. Add Subscriber")
        print("2. Remove Subscriber")
        print("3. display Subscriber")
        print("4. Notify All")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter subscriber name: ")
            sub = Subscriber(name)
            notifier.subscribe(sub)
            print(f" Done {name} subscribed.")

        elif choice == "2":
            name = input("Enter subscriber name to remove: ")
            for sub in notifier.subscribers:
                if sub.name == name:
                    notifier.unsubscribe(sub)
                    print(f" remove {name} unsubscribed.")
                    break
            else:
                print("Subscriber not found.")
        elif choice == "3":
            notifier.display()


        elif choice == "4":
            if not notifier.subscribers:
                print("No subscribers to notify.")
            else:
                notifier.notify("Notify New Notification!")

        elif choice == "5":
            print("Exiting app...")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == '__main__':
    main()