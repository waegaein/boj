import sys

def parse_input():
    inputs = list()

    # input = sys.stdin
    input = open('test.txt', 'r')
    for line in input.readlines():
        inputs.append([int(x) for x in line[:-1].split()])
    
    return inputs[1:]

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def get_next_prime(current_prime, upper_bound):
    for i in range(current_prime + 1, upper_bound + 1):
        if is_prime(i):
            return i

    return upper_bound

def prime_factorize(num, prime, prime_upper_bound):
    factors = list()

    if num > 1:
        if num % prime == 0:
            factors.append(prime)
            factors += prime_factorize(int(num / prime), prime, prime_upper_bound)
        else:
            factors += prime_factorize(num, get_next_prime(prime, prime_upper_bound), prime_upper_bound)

    return factors

def cleanse_factors(factors):
    cleansed = dict()
    for factor in factors:
        if factor in cleansed.keys():
            cleansed[factor] += 1
        else:
            cleansed[factor] = 1

    return cleansed

def get_lcm(num1, num2):
    lcm = 1

    num1_prime_factorized = cleanse_factors(prime_factorize(num1, get_next_prime(1, num1), num1))
    num1_prime_factors = set(num1_prime_factorized.keys())
    num2_prime_factorized = cleanse_factors(prime_factorize(num2, get_next_prime(1, num2), num2))
    num2_prime_factors = set(num2_prime_factorized.keys())
    for factor in num1_prime_factors.union(num2_prime_factors):
        if factor in num1_prime_factors and factor not in num2_prime_factors:
            lcm *= factor ** num1_prime_factorized[factor]
        elif factor not in num1_prime_factors and factor in num2_prime_factors:
            lcm *= factor ** num2_prime_factorized[factor]
        else:
            lcm *= factor ** max(num1_prime_factorized[factor], num2_prime_factorized[factor])

    return lcm

def run():
    inputs = parse_input()
    for num_pair in inputs:
        print(get_lcm(*num_pair))

run()
