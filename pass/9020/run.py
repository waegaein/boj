import sys


def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [int(line.strip()) for line in f.readlines()[1:]]


def get_bigger_prime_from_sieve(seive, current_prime):
    for i in range(current_prime+1, len(seive)):
        if seive[i]:
            return i

    return None


def get_primes_and_sieve(min, max):
    sieve = [False, False] + [True] * (max - 1)
    primes = list()
    prime = 2

    while prime is not None:
        if prime >= min:
            primes.append(prime)

        factor = prime
        current_index = prime * factor

        while current_index <= max:
            sieve[current_index] = False

            factor += 1
            current_index = prime * factor

        prime = get_bigger_prime_from_sieve(sieve, prime)

    return primes, sieve


def get_partitions(number, primes, sieve):
    partitions = list()
    prime_idx = 0
    prime = primes[prime_idx]

    while prime <= number // 2:
        partner = number - prime
        if sieve[partner]:
            partitions.append((prime, partner))

        prime_idx += 1
        prime = primes[prime_idx]

    return partitions


def get_partition_min_diff(number, primes, sieve):
    partitions = get_partitions(number, primes, sieve)

    return partitions[-1]


def main():
    numbers = parse_input()
    primes, sieve = get_primes_and_sieve(2, 10000)

    for number in numbers:
        prime, partner = get_partition_min_diff(number, primes, sieve)
        print(f'{prime} {partner}')

    return


main()
