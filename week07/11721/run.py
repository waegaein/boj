import sys

f = sys.stdin
# with open('test.txt', 'r') as f:
word = f.readline().strip()

idx_from = 0
while idx_from < len(word):
    print(word[idx_from:idx_from+10])
    idx_from += 10
