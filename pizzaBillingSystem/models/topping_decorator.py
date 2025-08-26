from .pizza import Pizza
from abc import ABC, abstractmethod

# Decorator
class ToppingDecorator(Pizza, ABC):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

