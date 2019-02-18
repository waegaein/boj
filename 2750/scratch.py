import sys

def parse_input():
    count = 0
    res = list()

    for line in sys.stdin:
        if count != 0:
            res.append(int(line))
        count += 1
    return res

def run():
    input = parse_input()
    input.sort()
    
    for i in input:
        print(i)

run()
