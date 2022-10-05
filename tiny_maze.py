import maze_generation

maze = maze_generation.generate_tiny([11, 11])
print(maze)

for index_1, x in enumerate(maze):
    for index_2, y in enumerate(x):
        wall_list = []
        split_string = [int(x) for x in str(y)]
        for num in split_string:
            wall_list.append(bool(num))
        maze[index_1][index_2] = {"walls": wall_list, "location": [index_1, index_2]}
        
file = open("mazegen3", "w")
file.write(str(maze))
file.close()