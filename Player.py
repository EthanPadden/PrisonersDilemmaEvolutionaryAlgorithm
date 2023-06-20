import traceback

import numpy as np
from Participant import Participant
import settings as g


class Player(Participant):
    def __init__(self, strategy_numbers=None):
        super().__init__()
        self.strategies = []
        g.initialise_strategies(self)
        if strategy_numbers is None:
            self.__strategy_numbers = np.random.randint(0, len(self.strategies), size=g.num_strategies_per_player)
        else:
            self.__strategy_numbers = strategy_numbers
        self.__points = 0
        self.__current_strategy_index = 0

    def to_string(self):
        return f"{''.join(map(str, self.__strategy_numbers))}\t{self.__points}"

    def add_points(self, points):
        self.__points += points

    def next_strategy(self):
        self.__current_strategy_index += 1

    def make_move(self, moves):
        try:
            strategy_num = self.__strategy_numbers[self.__current_strategy_index]
            strategy = self.strategies[strategy_num]
            # TODO: prob, now the indexes reference different methods - is that a concern? Now the output numbers do not mean anything to the user
            return strategy(moves)
        except Exception as e:
            print(traceback.format_exc())
            return None

    def reset_for_next_strategy(self):
        self.__temp_variables = {}
        self.__current_strategy_index = 0

    def get_points(self):
        return self.__points

    def get_strategies(self):
        return self.__strategy_numbers

    def reset_points(self):
        self.__points = 0

    def to_csv(self):
        return [
            ''.join(map(str, self.__strategy_numbers)),
            self.__points
        ]




