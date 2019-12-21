import sys
import math
from decimal import Decimal, ROUND_HALF_UP


def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return int(f.readline().strip())


def round_to_condition(num):
    return Decimal(str(num)).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)


def get_area_euclidean(r):
    return round_to_condition(r ** 2 * math.pi)


def get_area_taxi(r):
    return round_to_condition(r ** 2 * 2)


def main():
    r = parse_input()
    print(get_area_euclidean(r))
    print(get_area_taxi(r))

    return


main()
