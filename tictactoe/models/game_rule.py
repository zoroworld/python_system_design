class Game_rule:
    rule: str

    def __init__(self):
        self.rule = """
              1. Players take turns placing their symbol (X or O) on a 3x3 grid.
              2. The first player to align 3 of their symbols in a row, column, or diagonal wins.
              3. If all cells are filled and no player has won, the game is a draw.
              """