from .board import Board
from .dice import Dice
from .game_rule import GameRule


class Game(GameRule):
    def __init__(self):
        super().__init__()
        self.winner = ''

    def not_open_for_game(self, players):
        return [False for _ in players]

    def open_the_player_move(self, count, step, dice, player):
        print("---" * 40)
        if count == 6 and step < 3:  # allow up to 3 rerolls
            print(f"{player.name} with {player.symbol.SymbolType.value}  rolled a 6! 🎲 Roll again...")
            new_count = dice.dice_throw()
            print(f"Throw dice by {player.name} is {new_count}")
            return count + self.open_the_player_move(new_count, step + 1, dice, player)
        else:
            return count
        print("---" * 40)

    def start_game(self, players):
        #     greate the board have 10 x 10 grid means [ 1 to 100]
        board_len = 6
        print(self.rule)
        board = Board(board_len)
        get_board = board.get_board()
        snake_number = 6
        ladder_number = 6

        snakes, ladders = board.create_snake_and_ladder(get_board, snake_number, ladder_number)
        board.display_board()
        print("Snakes:", snakes)
        print("Ladders:", ladders)

        print("")

        dice = Dice()

        closedPlayer = self.not_open_for_game(players)

        #     each player turn will there
        print("----------------------Game Started----------------------")

        idx = 0

        while True:

            player = players[idx]

            print(f"Throw dice by {player.name} with {player.symbol.SymbolType.value}")
            value = input("Slide the dice by enter: ")
            print(value)

            if value == '':
                count = dice.dice_throw()
                print(f"Throw dice by {player.name} is {count}")

                if count == 6:
                    closedPlayer[idx] = True

                print(closedPlayer)

                if closedPlayer[idx] == True:
                    getvalue = self.open_the_player_move(count, 0, dice, player)
                    payer_new_pos = board.update_player_move(player, get_board, getvalue)
                    print(f"{player.name} moved to {payer_new_pos}")

                    # show updated board with players
                    print("------------------------------------")
                    board.display_board()
                    print("Snakes:", snakes)
                    print("Ladders:", ladders)
                    print("------------------------------------")

                    if payer_new_pos == board_len * board_len:
                        print(f"🎉 {player.name} wins the game! 🎉")
                        break
                        print("----------------GAME END--------------------")



            idx = (idx + 1) % len(players)

    #     if player go to stake they go down if ladder they go up
    #     take the snake and ladder any listoflist [[s,e],[e,s]]
    #     player go to 100 postion win the match
