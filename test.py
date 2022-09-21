"""thing"""
import random
from timeit import default_timer as timer
import maze_generation
# import maze_generation
# maze_generation.generate([2, 2])
#most effiecient
def t3(possible_moves):
    def ifTrue(x):
        return x[1]
    filter(ifTrue, possible_moves)
    if len(possible_moves):
        random_number = random.randint(0, len(possible_moves) -1)
        return possible_moves[random_number][0]
    return - 1


def t5(possible_moves):
    random_number = random.randint(0, len(possible_moves) - 1)
    return possible_moves[random_number]



maze_generation.generate([5, 5])
