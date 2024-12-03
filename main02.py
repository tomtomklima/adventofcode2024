# https://adventofcode.com/2024/day/2

MAX_STEP = 3

def __main__():
    #data = load_example()
    data = load_task()
    parsed_data = parse_input(data)

    safe_count = 0
    for level in parsed_data:
        if is_level_safe(level):
            safe_count += 1

    print(safe_count)

def is_level_safe(level):
    if len(level) <= 1:
        return True

    if level[0] == level[1]:
        return False
    elif level[0] < level[1]:
        asc = True
    else:
        asc = False

    for index, item in enumerate(level[:-1]):
        if asc:
           if level[index] >= level[index + 1]:
               return False
        else:
            if level[index] <= level[index + 1]:
                return False

        if abs(level[index] - level[index + 1]) > MAX_STEP:
            return False

    return True

def parse_input(input):
    return [[int(j) for j in i.split()] for i in input.split("\n")]

def load_example():
    f = open("task02example.txt", "r")

    return f.read()

def load_task():
    f = open("task02input.txt", "r")

    return f.read()

__main__()