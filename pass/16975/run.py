import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [[int(num) for num in line.strip().split()] for line in f.readlines()[1:]]

def run():
    inputs = parse_input()
    sequence = inputs[0]
    queries = inputs[2:]
    for query in queries:
        if query[0] == 1:
            i = query[1]
            j = query[2]
            k = query[3]
            for index in range(i-1, j):
                sequence[index] += k
        else:
            print(sequence[query[1]-1])

    return

run()
