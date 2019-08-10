import sys

def parse_input():
    input = sys.stdin
    # input = open('test.txt', 'r')

    return [line.strip() for line in input.readlines()[1:]]

def calculate_score(results):
    consecutive = 0
    score = 0
    for result in results:
        if result == 'O':
            consecutive += 1
            score += consecutive
        else:
            consecutive = 0

    return score

for case in parse_input():
    print(calculate_score(case))
