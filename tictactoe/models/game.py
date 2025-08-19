# models/game.py
from models.board import Board
from models.player import Player
from models.game_rule import Game_rule
from models.WiningStatergy import RowWinStrategy, ColumnWinStrategy, DiagonalWinStrategy
from models.WiningStatergy.game_winning import GameWinning
from models.bot import BotPlayer
from models.player_choose import PlayerChoose



class Game(Game_rule):
    def __init__(self):
        self.board = None
        super().__init__()

    def create_board(self):
        self.board = Board(3)
        return self.board.getBoard()

    def game_start_player(self, p1: Player, p2: Player):

        print("Game Rules___")
        print(self.rule)


        print("Game Started")
        self.create_board()



        play_list = [p1, p2]
        idx = 0



        self.board.display_board()

        winninggame = [
            GameWinning(RowWinStrategy()),
            GameWinning(ColumnWinStrategy()),
            GameWinning(DiagonalWinStrategy())
        ]



        while True:

            current_player = play_list[idx]
            print(f"{current_player.name}'s turn ({current_player.symbol})")

            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))

                # basic bounds check
                if not (0 <= row < 3 and 0 <= col < 3):
                    print("Invalid position. Try again.")
                    continue

                # check if cell is already filled
                if self.board.getBoard()[row][col].symbol != "":
                    print("Cell already taken. Try again.")
                    continue

                self.board.setBoard(row, col, current_player.symbol)

                # Display board state
                self.board.display_board()

                # Winning statergy

                flag = False
                for game in winninggame:
                    if game.winning(self.board.getBoard(), current_player.symbol):
                        flag = True

                if flag == True:
                    print(f"{'*' * 10}The winner is {current_player.name} {'*' * 10}")
                    break

                # switch player
                idx = 1 - idx


            except Exception as e:
                print(f"Error: {e}")

    def game_start_bot(self, p1: Player):
        print("Game Rules___")
        print(self.rule)

        print("Game Started")
        self.create_board()

        bot_player = Player("bot","O", "Bot")
        bot = BotPlayer(bot_player)
        player = p1

        play_list = [player, bot]

        idx = 0

        self.board.display_board()

        winninggame = [
            GameWinning(RowWinStrategy()),
            GameWinning(ColumnWinStrategy()),
            GameWinning(DiagonalWinStrategy())
        ]

        while True:

            current_player = play_list[idx]
            print(f"{current_player.name}'s turn ({current_player.symbol})")

            try:
                if idx != (len(play_list)-1):
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter col (0-2): "))
                else:
                    row, col = current_player.get_move(self.board)

                # basic bounds check
                if not (0 <= row < 3 and 0 <= col < 3):
                    print("Invalid position. Try again.")
                    continue
                elif not (row == -1, col == -1):
                    break

                # check if cell is already filled
                if self.board.getBoard()[row][col].symbol != "":
                    print("Cell already taken. Try again.")
                    continue

                self.board.setBoard(row, col, current_player.symbol)

                # Display board state
                self.board.display_board()


                flag = False
                for game in winninggame:
                    if game.winning(self.board.getBoard(), current_player.symbol):
                        flag = True

                if flag == True:
                    print(f"{'*' * 10}The winner is {current_player.name} {'*' * 10}")
                    break

                idx = 1 - idx



            except Exception as e:
                print(f"Error: {e}")







