import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return tuple(int(line.strip()) for line in f.readlines())

def run():
    inputs = parse_input()
    n = inputs[0]
    nums = inputs[1:-1]

    for num in nums:
        NOT = '' if num % n == 0 else 'NOT '
        print(f'{num} is {NOT}a multiple of {n}.')

    return

run()
