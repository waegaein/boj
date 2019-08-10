import sys

def parse_input():
    input = sys.stdin
    # input = open('test.txt', 'r')

    return [int(x.strip()) for x in input.readlines()]

acc = 1
for num in parse_input():
    acc *= num

res = dict()
for digit in str(acc):
    if digit in res.keys():
        res[digit] += 1
    else:
        res[digit] = 1

for i in range(10):
    stred = str(i)
    if stred in res.keys():
        print(res[stred])
    else:
        print(0)
