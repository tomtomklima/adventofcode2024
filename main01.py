# https://adventofcode.com/2024/day/1

def __main__():
    #data = load_example()
    data = load_task()
    parsed_data = parse_input(data)

    left_list = []
    right_list = []
    while parsed_data:
        left_list.append(int(parsed_data.pop(0)))
        right_list.append(int(parsed_data.pop(0)))

    left_list.sort()
    right_list.sort()

    #part 1
    #sum_diff = 0
    #while left_list and right_list:
    #    sum_diff += abs(left_list.pop() - right_list.pop())

    #print(sum_diff)

    #part 2
    right_list_histogram = dict()
    for right_number in right_list:
        try:
            right_list_histogram[right_number] += 1
        except KeyError:
            right_list_histogram[right_number] = 1

    sum_similarity = 0
    for left_number in left_list:
        try:
            sum_similarity += left_number * right_list_histogram[left_number]
        except KeyError:
            pass


    print(sum_similarity)

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