import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [int(num) for num in f.readlines()[1].strip().split()]

def get_frequencies(sequence):
    frequencies = dict()
    index = 0
    for num in sequence:
        if num in frequencies.keys():
            frequencies[num][1] += 1
        else:
            frequencies[num] = [index, 1]
            index += 1

    return list(frequencies.items())


def run():
    frequencies = get_frequencies(parse_input())
    frequencies = sorted(frequencies, key=lambda x: (-x[1][1], x[1][0]))

    print(' '.join([' '.join([str(frequency[0])] * frequency[1][1]) for frequency in frequencies]))

run()
