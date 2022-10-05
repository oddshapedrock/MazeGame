"""# TODO: """
import random

__all__ = [
"generate",
"generate_tiny",
"generate_3d"
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

    def generate_3d(self, maze_size):
        """ #TODO: """
        self.maze_size = maze_size

        self.grid_map = []

        for z_pos in range(maze_size[2]):
            self.grid_map.append([])
            #creates grid columns
            for y_pos in range(maze_size[1]):
                self.grid_map[z_pos].append([])
                for x_pos in range(maze_size[0]):
                    self.grid_map[z_pos][y_pos].append({
                        "walls": [True, True, True, True, True, True], #[forward, backward, left, right, up, down]
                        "visited": False,
                        "location": [x_pos, y_pos, z_pos] #[top, bottom]
                        })

        self.__make_path_3d()
        return self.grid_map
    
    def __get_pos_3d(self, x_pos, y_pos, z_pos):
        return self.grid_map[z_pos][y_pos][x_pos]
    
    def __get_possible_moves_3d(self):
        """# TODO: """
        moves_list = []
        snake_x = self.snake["location"][2]
        snake_y = self.snake["location"][1]
        snake_z = self.snake["location"][0]
        if snake_y + 1 < self.maze_size[1]:
            dir_forward = self.__get_pos_3d(snake_z, snake_y +1, snake_x)
            if not dir_forward["visited"]:
                moves_list.append(0)
        if snake_y -1 >= 0:
            dir_back = self.__get_pos_3d(snake_z, snake_y -1, snake_x)
            if not dir_back["visited"]:
                moves_list.append(1)
        if snake_x -1 >= 0:
            dir_left = self.__get_pos_3d(snake_z, snake_y, snake_x  -1)
            if not dir_left["visited"]:
                moves_list.append(2)
        if snake_x + 1 < self.maze_size[2]:
            dir_right = self.__get_pos_3d(snake_z, snake_y, snake_x +1)
            if not dir_right["visited"]:
                moves_list.append(3)
        if snake_z + 1 < self.maze_size[0]:
            dir_up = self.__get_pos_3d(snake_z +1, snake_y, snake_x)
            if not dir_up["visited"]:
                moves_list.append(4)
        if snake_z -1 >= 0:
            dir_down = self.__get_pos_3d(snake_z -1, snake_y, snake_x)
            if not dir_down["visited"]:
                moves_list.append(5)
        return moves_list
    
    def __new_visit_3d(self, location, location2, path):
        direction, opposite = path
        print(location2)
        self.__get_pos_3d(location[2], location[1], location[0])["walls"][path[0]] = False
        self.__get_pos_3d(location2[2], location2[1], location2[0])["walls"][path[1]] = False
        self.__get_pos_3d(location2[2], location2[1], location2[0])["visited"] = True
        self.snake["location"] = [location2[2], location2[1], location2[0]]
    
    def __make_path_3d(self):
        """# TODO: """
        starting_location = [0, 0, 0]
        self.__get_pos_3d(starting_location[2], starting_location[1], starting_location[0])["visited"] = True
        saved_locations = [starting_location]
        snake = self.snake
        snake["location"] = starting_location
        index = 0
        loop_number = (self.maze_size[0] * self.maze_size[1] * self.maze_size[2]) -1
        for _ in range(loop_number):
            self.__new_direction(self.__get_possible_moves_3d())
            while self.snake["direction"] == -1:
                if index == 0:
                    random.shuffle(saved_locations)
                self.snake["location"] = saved_locations[index]
                self.__new_direction(self.__get_possible_moves_3d())
                index += 1
            location = snake["location"]
            location2 = [location[2], location[1], location[0]]
            if snake["direction"] == 0:
                location2[1] += 1
                directions = [0, 1]
            if snake["direction"] == 1:
                location2[1] -= 1
                directions = [1, 0]
            if snake["direction"] == 2:
                location2[2] -= 1
                directions = [2, 3]
            if snake["direction"] == 3:
                location2[2] += 1
                directions = [3, 2]
            if snake["direction"] == 4:
                location2[0] += 1
                directions = [4, 5]
            if snake["direction"] == 5:
                location2[0] -= 1
                directions = [5, 4]
            self.__new_visit_3d(location, location2, directions)
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
generate_3d = _inst.generate_3d
