import sys


def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    result = list()
    num_test_cases = int(f.readline().strip())
    for i in range(num_test_cases):
        test_case = tuple(int(num) for num in f.readline().strip().split())
        result.append(test_case)

    return result


def get_distance_squared(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def get_the_number_of_cases(x1, y1, r1, x2, y2, r2):
    distance_squared = get_distance_squared(x1, y1, x2, y2)

    r_sum_squared = (r1 + r2) ** 2

    if r_sum_squared < distance_squared:
        return 0
    if r_sum_squared == distance_squared:
        return 1

    r_diff_squared = (r1 - r2) ** 2

    if r_diff_squared == 0 and distance_squared == 0:
        return -1

    if r_diff_squared > distance_squared:
        return 0
    if r_diff_squared == distance_squared:
        return 1

    return 2


def main():
    cases = parse_input()
    for case in cases:
        print(get_the_number_of_cases(*case))

    return


main()
