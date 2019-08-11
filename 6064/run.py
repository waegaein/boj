import sys
from math import gcd

def parse_input():
    # f = sys.stdin
    with open('test.txt', 'r') as f:
        return [[int(x) for x in line.split()] for line in f.read().strip().split('\n')[1:]]

def get_order(M, N, x, y):
    y_first = get_y_first_matching(M, N, x)
    ys_possible = get_ys_possible(M, N, x, y_first)
    order = x
    print(ys_possible)
    for y_possible in ys_possible:
        if y == y_possible:
            return order
        else:
            order += M

    return -1

def get_y_first_matching(M, N, x):
    if M <= N or x <= N:
        return x

    if x % N == 0:
        return x
    else:
        return x % N

def get_ys_possible(M, N, x, y_first):
    ys_possible = list()
    max_order = abs(M * N) // gcd(M, N)
    current_order = x
    current_y = y_first

    while current_order <= max_order:
        ys_possible.append(current_y)

        current_order += M
        current_y = get_y_next(M, N, current_y)

    return ys_possible

def get_y_next(M, N, current_y):
    y_candidate = current_y + M

    if y_candidate <= N:
        return y_candidate

    if y_candidate % N == 0:
        return N
    else:
        return y_candidate % N

def main():
    cases = parse_input()

    for case in cases:
        print(get_order(*case))

    return

main()

"""
39995 35557 12343 35052
39995 35557 12343 35051


1 1
2 2
3 3
4 1
5 2
6 3
7 1
1 2
2 3
3 1
4 2
5 3
6 1
7 2
1 3
2 1
3 2
4 3
5 1
6 2
7 3
"""
