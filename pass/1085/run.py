import sys


def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [int(num) for num in f.readline().strip().split()]


def get_shortest_anchor(x, y, w, h):
    return min(x, y, (w - x), (h - y))


def main():
    x, y, w, h = parse_input()

    print(get_shortest_anchor(x, y, w, h))

    return


main()
