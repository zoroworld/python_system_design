# models/board.py
from models.grid import Grid

class Board:
    def __init__(self, size: int):
        self.board_grid = []
        for i in range(size):
            row = []
            for j in range(size):
                cell = Grid(i, j, "")
                row.append(cell)
            self.board_grid.append(row)

    def getBoard(self):
        return self.board_grid

    def to_llm_string(self) -> str:
        """
        Convert board into a human-readable string (for LLMs).
        Empty cells are shown as ' '.
        """
        board = self.getBoard()
        return "\n".join([
            " | ".join(cell.symbol if cell.symbol != "" else " " for cell in row)
            for row in board
        ])



    def display_board(self):
        display_board = self.getBoard();
        n = len(display_board )
        for i in range(n):
            print(" --" * n*(n-1), end=" ")
            print()
            print(end="  |  ")
            for j in range(n):
                print(display_board[i][j].symbol, end="  |  ")
            print()
        print()

    def setBoard(self, row: int, col: int, symbol: str):
        self.board_grid[row][col].symbol = symbol
