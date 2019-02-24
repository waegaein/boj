import sys

def parse_input():
    infile = sys.stdin
    # infile = open('test.txt', 'r')

    return infile.readline()[:-1]

stripped = parse_input().strip()
print(0 if stripped is '' else len(stripped.split()))
