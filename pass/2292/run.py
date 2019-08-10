import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return int(f.readline().strip())

def get_min_blocks():
    destination = parse_input()
    n = 0
    acc = 0
    current_max = 1

    while destination > current_max:
        n += 1
        acc += n
        current_max = 1 + 6 * acc

    print(n + 1)

    return

get_min_blocks()
