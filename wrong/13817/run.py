import sys

def parse_input():
    # f = sys.stdin
    with open('test.txt', 'r') as f:
        return [[int(num) for num in line.split()] \
                for line in f.read().strip().split('\n')[:-1]]

def is_prime(num):
    if num == 2 or num == 3: return True
    if num < 2 or num % 2 == 0: return False
    if num < 9: return True
    if num % 3 == 0: return False

    r = int(num ** 0.5)
    f = 5
    while f <= r:
        if num % f == 0: return False
        if num % (f + 2) == 0: return False
        f += 6

    return True

def get_next_prime(prime):
    current = prime + 1
    while not is_prime(current):
        current += 1

    return current

def get_prime_factor(num):
    prime = 2
    while num % prime != 0:
        prime = get_next_prime(prime)

    return prime

def get_prime_factors(num):
    prime_factors = set()
    remaining = num
    while remaining != 1:
        factor = get_prime_factor(remaining)
        prime_factors.add(factor)
        remaining //= factor

    return prime_factors

def get_key(num):
    prime_factors = get_prime_factors(num)
    return max(prime_factors) - min(prime_factors)

def run():
    inputs = parse_input()
    for a, b in inputs:
        if get_key(a) > get_key(b):
            print('a')
        else:
            print('b')

run()
