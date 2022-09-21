"""# TODO: """
import random
import timeit
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
                    "isMaze": False,
                    "visited": False,
                    "location": [x_pos, y_pos] #[top, bottom]
                    })
        print(self.grid_map)

        self.new_direction([0,1,2,3])
        moves = self.get_possible_moves()
        print(moves)

    def new_direction(self, possible_moves):
        """# TODO: """
        random_number = random.randint(0, len(possible_moves) - 1)
        self.snake["direction"] = possible_moves[random_number]

    def get_pos(self, x_pos, y_pos):
        """# TODO: """
        return self.grid_map[x_pos][y_pos]

    def get_possible_moves(self):
        """# TODO: """
        moves_list = []
        snake_x = self.snake["location"][0]
        snake_y = self.snake["location"][1]
        if snake_y + 1 < self.maze_size[0]:
            dir_up = self.get_pos(snake_x, snake_y +1)
            if not dir_up["visited"] or dir_up.get["isMaze"]:
                moves_list.append(0)
        if snake_y -1 >= 0:
            dir_down = self.get_pos(snake_x, snake_y -1)
            if not dir_down["visited"] or dir_down["isMaze"]:
                moves_list.append(1)
        if snake_x -1 >= 0:
            dir_left = self.get_pos(snake_x -1, snake_y)
            if not dir_left["visited"] or dir_left["isMaze"]:
                moves_list.append(2)
        if snake_x + 1 < self.maze_size[0]:
            dir_right = self.get_pos(snake_x +1, snake_y)
            if not dir_right["visited"] or dir_right["isMaze"]:
                moves_list.append(3)

        return moves_list

    def make_path(self, starting_location):
        """# TODO: """
        saved_locations = [starting_location]
        snake = self.snake
        snake["location"] = starting_location
        while True:
            self.new_direction(self.get_possible_moves())
            break
        return

    def generate_tiny(self, maze_size):
        """# TODO: """
        generate(maze_size)

_inst = GenerateMaze()
generate = _inst.generate
generate_tiny = _inst.generate_tiny
