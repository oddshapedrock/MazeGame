import maze_generation
import os
import sys
sys.path.insert(0, os.getcwd() + '/mazes')

maze = maze_generation.generate_tiny([1000, 1000])
oldMaze = str(maze)

for index_1, x in enumerate(maze):
    for index_2, y in enumerate(x):
        wall_list = []
        split_string = [int(x) for x in str(y)]
        for num in split_string:
            wall_list.append(bool(num))
        maze[index_1][index_2] = {"walls": wall_list, "location": [index_1, index_2]}
        
file = open(os.getcwd() + "/mazes/mazegen3", "w")
file.write(oldMaze)
file.close()