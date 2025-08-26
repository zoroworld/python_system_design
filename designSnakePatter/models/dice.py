import random

class Dice:
    def __init__(self):
        self.size = 7


    def dice_throw(self):
        return random.randrange(1, self.size)