import sys


def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [tuple(int(num) for num in line.strip().split()) for line in f.readlines()[:-1]]


def is_right_triangle(first, second, third):
    if first >= second and first >= third:
        return first ** 2 == second ** 2 + third ** 2

    if second >= first and second >= third:
        return second ** 2 == first ** 2 + third ** 2

    if third >= first and third >= second:
        return third ** 2 == first ** 2 + second ** 2


def main():
    triples = parse_input()

    for triple in triples:
        if is_right_triangle(*triple):
            print('right')
        else:
            print('wrong')

    return


main()
