import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [int(line.strip()) for line in f.readlines()[:-1]]


def get_bigger_prime_from_sieve(seive, current_prime):
    for i in range(current_prime+1, len(seive)):
        if seive[i]:
            return i

    return None


def get_primes_from_sieve(min, max):
    sieve = [False, False] + [True] * (max - 1)
    primes = list()
    prime = 2

    while prime is not None:
        if prime > min:
            primes.append(prime)

        factor = prime
        current_index = prime * factor

        while current_index <= max:
            sieve[current_index] = False

            factor += 1
            current_index = prime * factor

        prime = get_bigger_prime_from_sieve(sieve, prime)

    return primes


def get_num_primes_in_interval(min, max):
    return len(get_primes_from_sieve(min, max))


def main():
    numbers = parse_input()

    for number in numbers:
        print(get_num_primes_in_interval(number, number * 2))

    return


main()
