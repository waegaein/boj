import sys
f = sys.stdin
# f = open('test.txt', 'r')

n = int(f.readline())
for i in range(n):
    print('*' * (i + 1))
