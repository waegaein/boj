import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [[int(x) for x in line.split()] for line in f.readlines()[1:]]

def get_room(floors, rooms_per_floors, nth):
    in_floor = (nth - 1) // floors + 1

    floor = (nth - 1) % floors + 1

    return f'{floor}{in_floor:02}'

def main():
    cases = parse_input()

    for case in cases:
        print(get_room(*case))

    return

main()
