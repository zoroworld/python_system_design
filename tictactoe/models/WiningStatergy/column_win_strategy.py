# strategies/column_win.py
from models.WiningStatergy.winning_strategy import WinningStrategy

class ColumnWinStrategy(WinningStrategy):
    def check(self, board, symbol) -> bool:
        for col in range(3):
            if all(board[row][col].symbol == symbol for row in range(3)):
                return True
        return False
