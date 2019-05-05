import sys

def parse_input():
    f = sys.stdin

    return int(f.read().strip())

def get_permutation(length):
    permutation_range = list(range(1, length+1))

    permutation = list()
    for i in range(length):
        permutation.append([permutation_range[i]])

    while len(permutation[0]) < length:
        permutation_appended = list()
        for sequence in permutation:
            for num in permutation_range:
                if num not in sequence:
                    permutation_appended.append(sequence + [num])
        permutation = permutation_appended

    return permutation

def run():
    num = parse_input()
    permutation = get_permutation(num)

    for sequence in permutation:
        print(' '.join([str(num) for num in sequence]))

    return

run()
