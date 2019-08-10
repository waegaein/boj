import sys

f = sys.stdin
# with open('test.txt', 'r') as f:
inputs = [[int(x) for x in line.strip().split()] for line in f.readlines()]

balance = sum(inputs[0])
price = inputs[1][0] * 2
if balance >= price:
    print(balance - price)
else:
    print(balance)
