
from .pizza import Pizza

# Concrete Component
class PlainPizza(Pizza):
    def get_description(self) -> str:
        return "Plain Pizza"

    def get_cost(self) -> float:
        return 100.0   # base price