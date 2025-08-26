from models.symbol_type import SymbolType
from models.symbol import Symbol
from models.player import Player
from models.game import Game

def main():
    # 1. create the player
    symbol1 = Symbol(SymbolType.RED)
    symbol2 = Symbol(SymbolType.GREEN)

    player1 = Player("AMIT",  symbol1)
    player2 = Player("SUMIT", symbol2)

    players = [player1, player2]

    # 2. start the game
    game = Game()
    game.start_game(players)

if __name__ == "__main__":
    main()