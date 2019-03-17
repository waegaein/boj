import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return int(f.read().strip())

def get_max_binary(digit):
    return int('0b' + ('1' * digit), 2)

max_binary = get_max_binary(parse_input())
acc = (max_binary + 1) * max_binary // 2

print(str(bin(acc))[2:])
