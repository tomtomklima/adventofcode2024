# https://adventofcode.com/2024/day/3

import re
from functools import reduce

def __main__():
    #data = load_example()
    data = load_task()
    parsed_data = parse_input(data)

    sum = 0
    for line in parsed_data:
        test_pattern = "mul\((\d{1,3}),(\d{1,3})\)"
        finds = re.findall(test_pattern, line)
        for find in finds:
            sum += reduce(lambda x, y: int(x) * int(y), find)

    print(sum)

def parse_input(input):
    return input.split("\n")

def load_example():
    f = open("task03example.txt", "r")

    return f.read()

def load_task():
    f = open("task03input.txt", "r")

    return f.read()

__main__()