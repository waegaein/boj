import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [[int(x) for x in line.split()] for line in f.readlines()[1:]]

def get_min_travels_required(distance):
    n = 0
    max_hop = 0
    current_max_distance = 0

    while distance > current_max_distance:
        if n % 2 == 0:
            max_hop += 1

        current_max_distance += max_hop
        n += 1

    return n

def main():
    distances = [pair[1] - pair[0] for pair in parse_input()]

    for distance in distances:
        print(get_min_travels_required(distance))

    return

main()
