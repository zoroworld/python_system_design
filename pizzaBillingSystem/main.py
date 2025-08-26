
from models import PlainPizza, Cheese, Pepperoni, Olives


def main():
    # Start with a plain pizza
    pizza = PlainPizza()
    print(f"{pizza.get_description()} => ₹{pizza.get_cost()}")

    # Add cheese
    pizza = Cheese(pizza)
    print(f"{pizza.get_description()} => ₹{pizza.get_cost()}")

    # Add pepperoni
    pizza = Pepperoni(pizza)
    print(f"{pizza.get_description()} => ₹{pizza.get_cost()}")

    # Add olives
    pizza = Olives(pizza)
    print(f"{pizza.get_description()} => ₹{pizza.get_cost()}")

if __name__ == "__main__":
    main()