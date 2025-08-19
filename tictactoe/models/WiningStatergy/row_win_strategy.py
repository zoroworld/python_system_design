# strategies/row_win.py
from models.WiningStatergy.winning_strategy import WinningStrategy

class RowWinStrategy(WinningStrategy):
    def check(self, board, symbol) -> bool:
        for row in board:
            if all(cell.symbol == symbol for cell in row):
                return True
        return False
