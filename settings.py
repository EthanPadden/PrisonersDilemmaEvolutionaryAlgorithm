from enum import Enum

from Participant import Participant

# Output
output_directory = 'output'
class GraphOption(Enum):
    SCATTER_PLOT_OBJECTIVE_SPACE = 0  # Scatter plot of total range vs total cost where each point is a solution in a population
    LINE_GRAPH_POINTS = 1  # Line graph of fitness (best/worst/avg) against generation number
    LINE_GRAPH_POINTS_STATS = 2  # Line graph of fitness (best/worst/avg) against generation number
graph_option = GraphOption.LINE_GRAPH_POINTS

# Initialisation
population_size = 6
num_strategies_per_player = 6

# Evaluation
num_rounds_per_game = 8

# Selection
num_selected_solns = 4

# Termination
max_generations = 6
percentage_performance_stagnation = 15

# Variation
crossover = True
mutation = True

# Strategies:
def initialise_strategies(instance):
    strategy_settings = [
        {instance.always_cooperate: True},
        {instance.always_defect: True},
        {instance.tit_for_tat: True},
        {instance.random: True},
        {instance.tit_for_2_tats: True},
        {instance.firm_but_fair: True},
        {instance.generous_tit_for_tat: True},
        {instance.soft_majority: True},
        {instance.hard_tit_for_tat: True},
        {instance.two_tits_for_tat: True},
        {instance.grim_trigger: True},
        {instance.suspicious_tit_for_tat: True},
        {instance.reverse_tit_for_tat: True},
        {instance.soft_grudger: True},
        {instance.hard_marjority: True},
        {instance.collective_strategy: True}
    ]
    for strategy_setting in strategy_settings:
        strategy_setting_key = list(strategy_setting.keys())[0]
        strategy_setting_value = strategy_setting[strategy_setting_key]
        if strategy_setting_value == True:
            instance.strategies.append(strategy_setting_key)
