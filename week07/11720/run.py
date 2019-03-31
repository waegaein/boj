import sys

f = sys.stdin
print(sum([int(x) for x in f.read().strip().split('\n')[1]]))
