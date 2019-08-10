import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [[x if not x.isdigit() else int(x) for x in line.strip().split()] for line in f.readlines()[1:]]

def get_sorted_by_composition(birthdays):
    return sorted(birthdays, key=lambda x: (x[3], x[2], x[1]))

def run():
    sorted = get_sorted_by_composition(parse_input())
    print(sorted[-1][0])
    print(sorted[0][0])

run()
