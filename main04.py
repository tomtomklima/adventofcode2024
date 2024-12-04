# https://adventofcode.com/2024/day/4
from ast import parse

def __main__():
    #data = load_example()
    #data = load_example_dots()
    data = load_task()
    parsed_data = parse_input(data)

    count = 0
    for y, line in enumerate(parsed_data):
        for x, character in enumerate(line):
            count += count_valid_eight_directions(parsed_data, x, y)

    print(count)

def count_valid_eight_directions(parsed_data, x, y):
    matrices = [
        [ # right
            [1,0],
            [2,0],
            [3,0],
        ],
        [ # right down
            [1,1],
            [2,2],
            [3,3],
        ],
        [ # down
            [0,1],
            [0,2],
            [0,3],
        ],
        [ # left down
            [-1,1],
            [-2,2],
            [-3,3],
        ],
        [ # left
            [-1,0],
            [-2,0],
            [-3,0],
        ],
        [ # left up
            [-1,-1],
            [-2,-2],
            [-3,-3],
        ],
        [ # up
            [0,-1],
            [0,-2],
            [0,-3],
        ],
        [ # up right
            [1,-1],
            [2,-2],
            [3,-3],
        ],
    ]

    count = 0
    for m in matrices:
        if (
                get_char_safely(parsed_data, x, y) == 'X'
            and get_char_safely(parsed_data, x+m[0][0], y+m[0][1]) == 'M'
            and get_char_safely(parsed_data, x+m[1][0], y+m[1][1]) == 'A'
            and get_char_safely(parsed_data, x+m[2][0], y+m[2][1]) == 'S'
        ):
            count += 1

    return count

def parse_input(input):
    return [list(i) for i in input.split("\n")]

def get_char_safely(parsed_data, y, x):
    if x < 0 or y < 0:
        return '.' # random invalid character

    try:
        return parsed_data[x][y]
    except IndexError:
        return '.'

def load_example():
    f = open("task04example.txt", "r")

    return f.read()

def load_example_dots():
    f = open("task04example_dots.txt", "r")

    return f.read()

def load_task():
    #f = open("task04input_crop.txt", "r")
    f = open("task04input.txt", "r")

    return f.read()

__main__()