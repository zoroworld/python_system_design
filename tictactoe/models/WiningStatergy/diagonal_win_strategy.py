# strategies/diagonal_win.py
from models.WiningStatergy.winning_strategy import WinningStrategy

class DiagonalWinStrategy(WinningStrategy):
    def check(self, board, symbol) -> bool:
        if all(board[i][i].symbol == symbol for i in range(3)):
            return True
        if all(board[i][2 - i].symbol == symbol for i in range(3)):
            return True
        return False
