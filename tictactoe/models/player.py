# models/player.py
from models.symbol import Symbol
from models.player_choose import PlayerChoose

class Player:
    def __init__(self, name: str, symbol: Symbol, player_choose: PlayerChoose):
        self.name = name
        self.symbol = symbol
        self.player_choose = player_choose

    def get_move(self, board):
        pass

