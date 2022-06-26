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
        pass

class human_player(player)