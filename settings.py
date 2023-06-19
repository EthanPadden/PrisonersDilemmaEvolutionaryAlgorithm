from enum import Enum

# Output
output_directory = 'output'
class GraphOption(Enum):
    SCATTER_PLOT_OBJECTIVE_SPACE = 0  # Scatter plot of total range vs total cost where each point is a solution in a population
    LINE_GRAPH_POINTS = 1  # Line graph of fitness (best/worst/avg) against generation number
    LINE_GRAPH_POINTS_STATS = 2  # Line graph of fitness (best/worst/avg) against generation number
graph_option = GraphOption.LINE_GRAPH_POINTS

# Initialisation
population_size = 6

# Selection
num_selected_solns = 4

# Termination
max_generations = 6

# TODO: options for what strategies to include