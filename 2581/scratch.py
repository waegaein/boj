import sys


def parse_input():
	infile = sys.stdin
	# infile = open('test1.txt', 'r')
	# infile = open('test2.txt', 'r')

	start = int(infile.readline())
	end = int(infile.readline())

	return start, end


def is_prime(num):
	if num == 1:
		return False

	for i in range(2, num):
		if num % i == 0:
			return False

	return True


def run():
	start, end = parse_input()
	primes = list()

	for num in range(start, end + 1):
		if is_prime(num):
			primes.append(num)

	if len(primes) == 0:
		print(-1)
		return
	else:
		print(sum(primes))
		print(primes[0])
		return


run()
