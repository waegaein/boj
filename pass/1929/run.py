import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [int(num) for num in f.read().strip().split('\n')[0].split()]

def sieve_with_min(max, min):
    def get_bigger_prime(seive, current_prime):
        for i in range(current_prime+1, len(seive)):
            if seive[i]:
                return i

        return None

    sieve = [False, False] + [True] * (max - 1)
    primes = list()
    prime = 2

    while prime is not None:
        if prime >= min:
            primes.append(prime)

        factor = prime
        current = prime * factor

        while current <= max:
            sieve[current] = False

            factor += 1
            current = prime * factor

        prime = get_bigger_prime(sieve, prime)

    return primes

def get_primes_in_interval():
    min, max = parse_input()

    print('\n'.join([str(prime) for prime in sieve_with_min(max, min)]))

    return

get_primes_in_interval()
