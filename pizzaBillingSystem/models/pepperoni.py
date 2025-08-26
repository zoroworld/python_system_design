from .topping_decorator import ToppingDecorator

# Concrete Decorators
class Pepperoni(ToppingDecorator):
    def get_description(self) -> str:
        return self._pizza.get_description() + ", Pepperoni"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 50.0