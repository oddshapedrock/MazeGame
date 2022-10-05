"""# TODO: """
import random

__all__ = [
"generate",
"generate_tiny"
]

class GenerateMaze():
    '''Generates a maze of [width, height] size as a python dictionary'''
    def __init__(self):
        self.maze_size = [0, 0]
        self.grid_map = []
        self.snake = {"direction": 0, "location": [0, 0], "number": 1}

    def generate(self, maze_size):
        '''Generates a maze of [width, height] size as a python dictionary'''
        self.maze_size = maze_size

        self.grid_map = []

        #creates grid rows
        for x_pos in range(maze_size[0]):
            self.grid_map.append([])
            #creates grid columns
            for y_pos in range(maze_size[1]):
                self.grid_map[x_pos].append({
                    "walls": [True, True, True, True], #[top, bottom, left, right]
                    "visited": False,
                    "location": [x_pos, y_pos] #[top, bottom]
                    })

        self.__make_path()
        return self.grid_map

    def __new_direction(self, possible_moves):
        """# TODO: """
        if possible_moves:
            random_number = random.randint(0, len(possible_moves) - 1)
            self.snake["direction"] = possible_moves[random_number]
        else:
            self.snake["direction"] = -1

    def __get_pos(self, x_pos, y_pos):
        """# TODO: """
        return self.grid_map[x_pos][y_pos]

    def __get_possible_moves(self):
        """# TODO: """
        moves_list = []
        snake_x = self.snake["location"][0]
        snake_y = self.snake["location"][1]
        if snake_y + 1 < self.maze_size[0]:
            dir_up = self.__get_pos(snake_x, snake_y +1)
            if not dir_up["visited"]:
                moves_list.append(0)
        if snake_y -1 >= 0:
            dir_down = self.__get_pos(snake_x, snake_y -1)
            if not dir_down["visited"]:
                moves_list.append(1)
        if snake_x -1 >= 0:
            dir_left = self.__get_pos(snake_x -1, snake_y)
            if not dir_left["visited"]:
                moves_list.append(2)
        if snake_x + 1 < self.maze_size[0]:
            dir_right = self.__get_pos(snake_x +1, snake_y)
            if not dir_right["visited"]:
                moves_list.append(3)
        return moves_list

    def __new_visit(self, location, x_pos2, y_pos2, path):
        direction, opposite = path
        self.__get_pos(location[0], location[1])["walls"][direction] = False
        self.__get_pos(x_pos2, y_pos2)["walls"][opposite] = False
        self.__get_pos(x_pos2, y_pos2)["visited"] = True
        self.snake["location"] = [x_pos2, y_pos2]

    def __make_path(self):
        """# TODO: """
        starting_location = [0, 0]
        self.__get_pos(starting_location[0], starting_location[1])["visited"] = True
        saved_locations = [starting_location]
        snake = self.snake
        snake["location"] = starting_location
        index = 0
        loop_number = (self.maze_size[0] * self.maze_size[1]) -1
        for _ in range(loop_number):
            self.__new_direction(self.__get_possible_moves())
            while self.snake["direction"] == -1:
                if index == 0:
                    random.shuffle(saved_locations)
                self.snake["location"] = saved_locations[index]
                self.__new_direction(self.__get_possible_moves())
                index += 1
            location = snake["location"]
            if snake["direction"] == 0:
                self.__new_visit(location, location[0], location[1] + 1, [0, 1])
            if snake["direction"] == 1:
                self.__new_visit(location, location[0], location[1] - 1, [1, 0])
            if snake["direction"] == 2:
                self.__new_visit(location, location[0] -1, location[1], [2, 3])
            if snake["direction"] == 3:
                self.__new_visit(location, location[0] +1, location[1], [3, 2])
            saved_locations.append(snake["location"])


    def generate_tiny(self, maze_size):
        """# TODO: """
        tiny_map = []
        grid_map = generate(maze_size)
        for index, grid in enumerate(grid_map):
            tiny_map.append([])
            for cell in grid:
                string = ""
                for index2 in range(4):
                    if cell["walls"][index2]:
                        string += "1"
                    else:
                        string += "0"
                tiny_map[index].append(string)
        return tiny_map  

_inst = GenerateMaze()
generate = _inst.generate
generate_tiny = _inst.generate_tiny
