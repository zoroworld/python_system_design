
from models.WiningStatergy.winning_strategy import WinningStrategy

class GameWinning:
    def __init__(self, winning_strategy: WinningStrategy):
        self.winning_strategy = winning_strategy

    def winning(self, board, symbol):
        return self.winning_strategy.check(board, symbol)
