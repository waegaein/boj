import sys

def read_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return f.read().strip().split('\n')[1:]

def parse_input(input):
    res = list()
    for line in input:
        if ' ' not in line:
            res.append(list())
        else:
            splitted = line.split()
            credit = int(splitted[0])
            grade = float(splitted[1])
            res[len(res)-1].append((credit, grade))

    return res

def run():
    inputs = parse_input(read_input())
    for input in inputs:
        credits = sum(x[0] * x[1] for x in input)
        grades = sum(x[0] for x in input)
        print(grades, round(credits/grades, 1))

run()
