import sys

f = sys.stdin
# f = open('test.txt', 'r')

scores = [int(score) if int(score) >= 40 else 40 for score in f.read().split('\n') if score.isdigit()]

print(int(sum(scores) / len(scores)))
