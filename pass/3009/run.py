import sys


def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [tuple(int(num) for num in line.strip().split()) for line in f.readlines()]


def get_missing_point(others):
    x_frequencies = dict()
    y_frequencies = dict()

    for x, y in others:
        if x not in x_frequencies.keys():
            x_frequencies[x] = 1
        else:
            x_frequencies[x] += 1

        if y not in y_frequencies.keys():
            y_frequencies[y] = 1
        else:
            y_frequencies[y] += 1

    for x, freq in x_frequencies.items():
        if freq == 1:
            missing_x = x

    for y, freq in y_frequencies.items():
        if freq == 1:
            missing_y = y

    return missing_x, missing_y


def main():
    points = parse_input()
    print(' '.join([str(num) for num in get_missing_point(points)]))

    return


main()
