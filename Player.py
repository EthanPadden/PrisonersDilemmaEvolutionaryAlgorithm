import numpy as np
from Participant import Participant


class Player(Participant):
    num_strategies = 6
    def __init__(self, strategies=None):
        super().__init__()
        if strategies is None:
            self.__strategies = np.random.randint(0, len(self.strategies), size=Player.num_strategies)
        else:
            self.__strategies = strategies
        self.__points = 0
        self.__current_strategy_index = 0

    def to_string(self):
        return f"{''.join(map(str, self.__strategies))}\t{self.__points}"

    def add_points(self, points):
        self.__points += points

    def next_strategy(self):
        self.__current_strategy_index += 1

    def reset_strategy_index(self):
        self.__current_strategy_index = 0

    def make_move(self, moves):
        strategy_num = self.__strategies[self.__current_strategy_index]
        strategy = self.strategies[strategy_num]
        return strategy(moves)

    def get_points(self):
        return self.__points

    def get_strategies(self):
        return self.__strategies

    def to_csv(self):
        return [
            ''.join(map(str, self.__strategies)),
            self.__points
        ]




