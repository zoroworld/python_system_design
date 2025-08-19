from models.player import Player
from models.game import Game
# from models.symbol import Symbol


def main():
    print("""
    1. Play to play with player
    2. Play with bot
    """)

    choose = int(input("optiion 1 or 2: "))
    if choose == 1:
        p1 = Player("Ali", "X", "Human")
        p2 = Player("Shiva", "O", "Human")

        game = Game()
        game.game_start_player(p1, p2)

    else:
        p1 = Player("Ali", "X", "Human")

        game = Game()
        game.game_start_bot(p1)



if __name__ == "__main__":
    main()
