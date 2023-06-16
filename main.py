import csv
from datetime import datetime
import strategies as s

import numpy as np

from Player import Player

if __name__ == '__main__':
    '''
    Prisoner's Dilemma terminology used here:
        Cooperate = stay loyal to opponent  (deny)
        Defect = snitch on opponent         (confess/betray)
        
        TODO: allow for variables here rather than hard coded values
        PAYOFF MTX: A/B - where points DO NOT represent sentence years - represent points won (higher = BETTER)
                    B Defect	B Cooperate
        A Defect	   2/2	     10/1
        A Cooperate	   1/10      3/3
        
        Move = cooperate/defect
        Strategy = always cooperate, always defect, tit-for-tat etc
    '''

    '''
    Each solution will be a collection of D preset strategies (always cooperate, always defect, tit-for-tat, etc)
        This can be represented as an array of D integers, where each integer corresponds to a strategy according to an enum,
        the value of which is a function outlining how the player comes up with the move
    In every generation, a player will play each strategy against D other opponents, N times
    Each opponent will have a random strategy
    The objective values will be the accumulated points over N games
    Termination will be determined by a max number of generations
    Selection will be done by sorting solution by objective values and selecting the top solutions (the number of which will be a variable in settings)
    Variation:
        Crossover: take the first rounded D/2 strategies from parent A and the second rounded D/2 strategies from parent B
        Mutation: change a random strategy to some other random strategy
    '''

    output_filename = f"output/output {datetime.now().strftime('Y-%m-%d_%H-%M-%S.csv')}"
    population_size = 6

    with open(output_filename, 'w', newline='') as file:
        writer = csv.writer(file)

        # INITIALISATION    ===================================
        current_gen = []
        for i in range(0, population_size):
            current_gen.append(Player())

        writer.writerow(['STAGE', 'INITIALISATION'])
        for solution in current_gen:
            print(solution.to_string())
        writer.writerow(current_gen)


