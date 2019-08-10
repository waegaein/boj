import sys

def parse_input():
    f = sys.stdin
    f = open('test3.txt', 'r')

    return int(f.read().strip())

def count_digits(num):
    return len(str(num))

def get_span_minimum(digits):
    return (10 ** (digits - 1)) * digits

def run():
    num = parse_input()

    digits = count_digits(num)
    while num < get_span_minimum(digits):
        digits -= 1

    print(int(num / digits))

run()
