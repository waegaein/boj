import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [[int(num) for num in line.strip().split()] for line in f.readlines()[1:]]

def apply_query_1(sequence, i, j , k):
    for index in range(i-1, j):
        sequence[index] += k

    return sequence

def apply_query_2(sequence, index):
    print(sequence[index-1])

    return

def run():
    inputs = parse_input()
    sequence = inputs[0]
    queries = inputs[2:]
    for query in queries:
        if query[0] == 1:
            sequence = apply_query_1(sequence, *query[1:])
        else:
            apply_query_2(sequence, query[1])

    return

run()
