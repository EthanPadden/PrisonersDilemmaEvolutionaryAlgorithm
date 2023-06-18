from random import randint

from Participant import Participant


class Opponent(Participant):
    def __init__(self):
        self.__points = 0

    def add_points(self, points):
        self.__points += points
