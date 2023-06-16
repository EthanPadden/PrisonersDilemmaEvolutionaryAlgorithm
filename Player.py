import strategies as s
import numpy as np
class Player:
    num_strategies = 6
    def __init__(self):
        self.__strategies = np.random.randint(0, len(s.strategies), size=Player.num_strategies)
        self.__total_points = 0

    def to_string(self):
        return f"{''.join(map(str, self.__strategies))}\t{self.__total_points}"


