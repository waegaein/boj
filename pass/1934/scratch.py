import sys
from math import gcd

def parse_input():
    f = sys.stdin
    with open('test.txt', 'r') as f:
        return [tuple(int(num) for num in line.strip().split()) for line in f.readlines()][1:]

def get_lcm(x, y):
   return abs(x * y) // gcd(x, y)

def run():
    inputs = parse_input()
    for num_pair in inputs:
        print(get_lcm(*num_pair))

run()
