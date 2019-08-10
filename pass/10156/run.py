import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [int(x) for x in f.read().strip().split()]

input = parse_input()
price = input[0]
quantity = input[1]
cash = input[2]

short_of = price * quantity - cash
print(short_of if short_of > 0 else 0)
