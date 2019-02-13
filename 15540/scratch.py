m = 2002
a = 4
b = 11


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


def get_p_range_rev(m):
	return reversed(range(1, int(m ** 0.5) + 1))


def get_q_range_rev(m, a, b, p):
	upper_bound_by_product = int(m / p)
	upper_bound_by_ratio = int(b/a * p)
	return reversed(range(p, min(upper_bound_by_product, upper_bound_by_ratio) + 1))


def get_most_suitable(m, a, b):
	res = list()

	for p in get_p_range_rev(m):
		if is_prime(p):
			for q in get_q_range_rev(m, a, b, p):
				if is_prime(q):
					res.append((p, q, p*q))
					break

	return max(res, key=lambda triplet: triplet[2])[:2]


print(get_most_suitable(m, a, b))
