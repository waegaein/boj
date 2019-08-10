import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return int(f.readline().strip())

def get_fraction():
    target = parse_input()

    n = 0
    acc = 0
    current_diagonal = 1

    while target >= current_diagonal:
        previous_diagonal = current_diagonal

        n += 1
        acc += n
        current_diagonal = 1 + 4 * acc

    numerator = n
    denominator = n

    remaining = target - previous_diagonal

    while remaining > 0:
        if (numerator + denominator) % 2 == 0:
            if numerator == 1:
                denominator += 1
            else:
                numerator -= 1
                denominator += 1
        else:
            if denominator == 1:
                numerator += 1
            else:
                numerator += 1
                denominator -= 1

        remaining -= 1

    print(f'{numerator}/{denominator}')

    return

get_fraction()
