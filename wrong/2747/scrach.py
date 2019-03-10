import sys
sys.setrecursionlimit(6000)
def parse_input():
    input = sys.stdin
    # input = open('test.txt', 'r')

    return int(input.readline())

fib_list = [None] * (parse_input() + 1)

def get_fib(n):
    if fib_list[n] is None:
        if n < 2:
            fib_list[n] = n
        else:
            fib_list[n] = get_fib(n-1) + get_fib(n-2)

    return fib_list[n]


print(get_fib(parse_input()))
