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

    def generate(self, maze_size):
        '''Generates a maze of [width, height] size as a python dictionary'''
        self.maze_size = maze_size

        self.grid_map = []

        #creates grid rows
        for x_pos in range(maze_size[0]):
            self.grid_map.append([])
            #creates grid columns
            for y_pos in range(maze_size[1]):
                self.grid_map[x_pos].append([{
                    "walls": [True, True, True, True], #[top, bottom, left, right]
                    "isMaze": False,
                    "visited": False,
                    "location": [x_pos, y_pos] #[top, bottom]
                    }])
        print(self.grid_map)

        snake = {"direction": 0, "location": [0, 0]}

        snake["direction"] = self.new_direction([True, True, True, True])
        print(snake)

    def new_direction(self, possible_moves):
        """# TODO: """
        amount = -1
        for direction in possible_moves:
            if direction:
                amount += 1

        if not amount == -1:
            random_number = random.randint(0, amount)
            index = 0
            while index < len(possible_moves):
                if possible_moves[index] and not random_number:
                    return index
                index += 1
                random_number -= 1
        return -1

    def generate_tiny(self, maze_size):
        """# TODO: """
        generate(maze_size)

_inst = GenerateMaze()
generate = _inst.generate
generate_tiny = _inst.generate_tiny
