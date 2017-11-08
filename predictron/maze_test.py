from maze import MazeGenerator
g = MazeGenerator(height=4, width=4, density=0.15)
mazes = g.generate_mazes(1)
from pprint import pprint
pprint(mazes[0])
print(g.get_trajectory(mazes[0]))
