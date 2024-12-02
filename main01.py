# https://adventofcode.com/2024/day/1
import urllib.request
from ast import parse


def __main__():
    #data = load_example()
    data = load_task()
    parsed_data = parse_input(data)

    left_list = []
    right_list = []
    while parsed_data:
        left_list.append(int(parsed_data.pop()))
        right_list.append(int(parsed_data.pop()))

    left_list.sort()
    right_list.sort()

    sum = 0
    while left_list and right_list:
        sum += abs(left_list.pop() - right_list.pop())

    print(sum)

def parse_input(input):
    return input.split()

def load_example():
    return """3   4
4   3
2   5
1   3
3   9
3   3"""

def load_task():
    f = open("task01.txt", "r")

    return f.read()

__main__()