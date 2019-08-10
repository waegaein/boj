import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return tuple(tuple(int(x) for x in line.strip().split()) for line in f.readlines())

def run():
    inputs = parse_input()
    height = inputs[0][1]
    fruits = sorted(inputs[1])
    for fruit in fruits:
        if height >= fruit:
            height += 1

    print(height)

run()
