import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return tuple(line.strip() for line in f.readlines()[1:])

def run():
    inputs = parse_input()
    yesterday = inputs[0]
    today = inputs[1]
    count = 0
    for i in range(len(yesterday)):
        if yesterday[i] == 'C' and today[i] == 'C':
            count += 1

    print(count)

run()
