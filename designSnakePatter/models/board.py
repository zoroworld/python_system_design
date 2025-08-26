import random

from .grid import Grid

class Board:
    def __init__(self, size):
        self.board = []
        self.snakes = []
        self.ladders = []

        self.create_board(size)

    def create_board(self, size):
        for row in range(size):
            row_cells = []
            for col in range(size):
                num = (size * row) + col + 1
                grid = Grid(row, col, "", num)
                row_cells.append(grid)

            if row % 2 == 1:
                row_cells.reverse()

            self.board.append(row_cells)

    def display_board(self):

        for row in range(len(self.board)):
            print("")
            for col in range(len(self.board)):
                print("|", end=" ")
                print([self.board[row][col].num, self.board[row][col].symbol] , end=" ")
        print("\n")

    def get_board(self):
        return self.board

    def get_board_size(self, board):
        return len(board)

    def create_snake_and_ladder(self, board, num_snakes, num_ladders):

        use_position = set()
        board_size = self.get_board_size(board) * self.get_board_size(board)

        # generate snake
        tries = 0
        tries_limit = 10000
        while len(self.snakes) < num_snakes and tries < tries_limit:

            head = random.randrange(2, board_size)
            tail = random.randrange(1, head)

            if head not in use_position and tail not in use_position:
                self.snakes.append([head, tail])
                use_position.add(head)
                use_position.add(tail)
            tries += 1

        tries = 0
        while len(self.ladders) < num_ladders and tries < tries_limit:
            bottom = random.randrange(2, board_size - 1)
            top = random.randrange(bottom + 1, board_size + 1)

            if top not in use_position and bottom not in use_position:
                self.ladders.append([bottom, top])
                use_position.add(bottom)
                use_position.add(top)
            tries += 1

        return self.snakes, self.ladders


    def snake_and_ladders(self, player, new_pos):
        print("Check by snake and ladder")


        for head in  range(len(self.snakes)):
            if self.snakes[head][0] == new_pos:
                print(f"{player.name} got bitten by snake! {new_pos} → {self.snakes[head][1]}")
                new_pos = self.snakes[head][1]
                break;

        for bottom in  range(len(self.ladders)):
            if self.ladders[bottom][0] == new_pos:
                print(f"{player.name} climbed a ladder! {self.ladders[bottom][1]}")
                new_pos = self.ladders[bottom][1]
                break;

        return new_pos


    def update_player_move(self, player, board, steps):

        for i in range(len(board)):
            for j in range(len(board)):
                if player.position == board[i][j].num:
                    board[i][j].symbol = ""

        new_pos = player.position + steps
        max_pos = len(board) * len(board)

        if new_pos > max_pos:
            new_pos = player.position

        new_pos = self.snake_and_ladders(player, new_pos)

        for i in range(len(board)):
            for j in range(len(board)):
                if new_pos == board[i][j].num:
                    board[i][j].symbol = board[i][j].symbol + player.symbol.SymbolType.value

        player.position = new_pos
        return new_pos







