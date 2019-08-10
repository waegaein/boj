import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [int(line.strip()) for line in f.readlines()]

def get_average(num_list):

    return sum(num_list) // len(num_list)

def get_median(num_list):
    num_list_sorted = sorted(num_list)

    return num_list_sorted[len(num_list) // 2]

def run():
    num_list = parse_input()

    print(get_average(num_list))
    print(get_median(num_list))

    return

run()
