from random import randint


class Opponent:
    def make_move(self):
        random_number = randint(0, 100)
        self.__points = 0
        return (random_number > 50)

    def add_points(self, points):
        self.__points += points
