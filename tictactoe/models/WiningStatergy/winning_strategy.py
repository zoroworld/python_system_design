# strategies/winning_strategy.py
from abc import ABC, abstractmethod
class WinningStrategy(ABC):
    @abstractmethod
    def check(self, board, Symbol) -> bool:
        pass
