import math
import random

class player:
    def __init__(self,letter):
        self.letter = letter
    def get_move(self,game):
        pass

class random_computer_player(player):
    def __init__(self,letter):
        super().__init__(letter)
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class human_player(player)
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')