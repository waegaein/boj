import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return int(f.readlines()[0].strip())

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def main():
    print(factorial(parse_input()))

main()
