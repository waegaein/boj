import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [int(line.strip()) for line in f.readlines()][1:]

def get_changes(price):
    quarters = price // 25
    price %= 25

    dimes = price // 10
    price %= 10

    nickels = price // 5
    price %= 5

    pennies = price

    return quarters, dimes, nickels, pennies

def run():
    test_cases = parse_input()
    for test_case in test_cases:
        print(' '.join([str(change) for change in get_changes(test_case)]))

    return

run()
