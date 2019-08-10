import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return int(f.read().strip())

def get_sigma_result(num):
    sigma = 0
    i = 1
    while i ** 2 <= num:
        if num % i == 0:
            sigma += i
            sigma += num // i

        i += 1

    return sigma

def run():
    print(get_sigma_result(parse_input()))

run()
