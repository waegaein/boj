import sys

def parse_input():
    # f = sys.stdin
    with open('test.txt', 'r') as f:
        return [int(line.strip()) for line in f.read().splitlines()]

def get_sum_remainder(k):
    return ((k * (k - 1)) // 2) % k

def main():
    parsed = parse_input()

    left = parsed[0]
    right = parsed[1]
    k = parsed[2]

    rem = get_sum_remainder(k)

    count = 0
    for num in range(2 * k + rem , right + 1):
        if num % k == rem:
            count += 1

    print(count)

    return

main()
