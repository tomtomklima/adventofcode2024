# https://adventofcode.com/2024/day/3

import re
from functools import reduce

def __main__():
    #data = load_example()
    data = load_task()
    parsed_data = parse_input(data)

    sum = 0
    test_pattern_first_find = "mul\((\d{1,3}),(\d{1,3})\)"
    first_find = re.search(test_pattern_first_find, parsed_data[0])
    sum += reduce(lambda x, y: int(x) * int(y), first_find.groups())

    for line in parsed_data:
        test_pattern = "(?<=do\(\))(?:.*?)mul\((\d{1,3}),(\d{1,3})\)"
        # currently will not work - must find ALL `mul()` after `do()` instruction
        # currently only first one is found
        finds = re.findall(test_pattern, line)
        for find in finds:
            sum += reduce(lambda x, y: int(x) * int(y), find)

    print(sum)

def parse_input(input):
    return input.split("\n")

def load_example():
    #f = open("task03example.txt", "r")
    f = open("task03example_second_part.txt", "r")

    return f.read()

def load_task():
    f = open("task03input.txt", "r")

    return f.read()

__main__()