import sys

def parse_input():
    # infile = sys.stdin
    infile = open('test.txt', 'r')

    input_line = infile.readline().split(' ')

    res = list()
    for i in input_line:
        res.append(int(i))

    return res

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

def get_primes(interval):
    primes = list()

    while len(interval) != 0:
        head = interval[0]
        if is_prime(head):
            primes.append(head)
        interval = [x for x in interval if x % head != 0]

    return primes

def run():
    input = parse_input()
    start = input[0]
    end = input[1]

    interval = list(range(start, end + 1))
    primes = get_primes(interval)

    for prime in primes:
        print(prime)

    return

run()
