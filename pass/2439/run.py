import sys

input = int(sys.stdin.read().strip().split('\n')[0])
for i in range(1, input+1):
    print(' ' * (input-i) + '*' * i)
