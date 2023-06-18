import csv
import math
import traceback
from datetime import datetime
import random

import strategies as s

import numpy as np

from Game import Game
from Player import Player

def evaluate(player):
    for i in range(0, Player.num_strategies):
        game = Game(player)
        game.play()
        player.next_strategy()


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
    Selection will be done by sorting solution by objective values and selecting the top  solutions (the number of which will be a variable in settings)
    Variation:
        Crossover: take the first rounded D/2 strategies from parent A and the second rounded D/2 strategies from parent B
        Mutation: change a random strategy to some other random strategy
    '''

    output_filename = f"output/output {datetime.now().strftime('Y-%m-%d_%H-%M-%S.csv')}"
    population_size = 6
    num_selected_solns = 4
    max_generations = 6

    with open(output_filename, 'w', newline='') as file:
        writer = csv.writer(file)

        # INITIALISATION    ===================================
        current_gen = []
        for i in range(0, population_size):
            current_gen.append(Player())

        for solution in current_gen:
            print(solution.to_string())

        #TODO: is the 0 argument in the range function necessary when used for 0 to value (not inclusive of the upper limit)?
        for gen in range(0, max_generations):
            try:
                # EVALUATION
                for player in current_gen:
                    player.reset_strategy_index()
                    evaluate(player)
                    print(player.get_points())
                    output = []
                    output.append(gen)
                    output.append(player.to_csv()[0])
                    output.append(player.to_csv()[1])
                    writer.writerow(output)


                # SELECTION
                sorted_solutions = sorted(current_gen, key=lambda solution: solution.get_points(), reverse=True)
                next_gen = []
                for i in range(0, num_selected_solns):
                    next_gen.append(sorted_solutions[i])

                # VARIATION
                # crossover
                print(sorted_solutions)
                print(next_gen)

                while (len(next_gen) < population_size):
                    # choose the top 2 in the population - and pop them off so we dont consider them anymore
                    parent_a = current_gen.pop(0)
                    parent_b = current_gen.pop(0)
                    # CROSSOVER HERE
                    # offspring_c, offspring_d = tools.crossover(parent_a, parent_b)
                    # ceil rather than floor - if we need to take 1 more from either parent it should be the one that has more points
                    crossover_point = math.ceil(Player.num_strategies / 2)
                    strategies_parent_a = parent_a.get_strategies()
                    strategies_parent_b = parent_b.get_strategies()

                    strategies_offspring_c = np.concatenate((strategies_parent_a[:crossover_point], strategies_parent_b[crossover_point:]))
                    strategies_offspring_d = np.concatenate((strategies_parent_b[:crossover_point], strategies_parent_a[crossover_point:]))
                    offspring_c = Player(strategies_offspring_c)
                    offspring_d = Player(strategies_offspring_d)

                    # ADD SOLNS TO NEXT GEN
                    next_gen.append(offspring_c)
                    if len(next_gen) < population_size:
                        next_gen.append(offspring_d)

                # mutation
                # choose a random number of players in next generation
                num_players_to_mutate = random.randint(1, population_size)
                for i in range(1, num_players_to_mutate):
                    # choose a random player
                    player_index_to_mutate = random.randint(0, (population_size - 1))
                    player_to_mutate = next_gen[player_index_to_mutate]

                    # choose a random number of strategies to change? TODO
                    # choose a random strategy to change and a random value to change it to
                    strategy_index_to_change = random.randint(0, (Player.num_strategies - 1))
                    #TODO: ensure this is not the same as before?
                    # TODO: check if these range endpoints are includive/exclusive - currently assuming both inclusive
                    value_to_change_to = random.randint(0, (len(s.strategies)-1))

                    player_to_mutate.get_strategies()[strategy_index_to_change] = value_to_change_to
                    # TODO: more efficient way

                current_gen = next_gen
            except Exception as e:
                print(f'GENERATION: {gen}')
                print(traceback.format_exc())
                exit()