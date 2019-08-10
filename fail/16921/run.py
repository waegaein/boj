import sys

def parse_input():
    f = sys.stdin
    with open('test.txt', 'r') as f:
        return int(f.readline().strip())

def run():
    num = parse_input()
    sequences = [[1], [5], [10], [50]]

    for i in range(num-1):
        sequences_new = list()
        
        for sequence in sequences:
            current = sequence
            sequences_new.append(current + [1])
            sequences_new.append(current + [5])
            sequences_new.append(current + [10])
            sequences_new.append(current + [50])

        sequences = sequences_new

    decimals = set()
    for sequence in sequences:
        decimals.add(sum(sequence))

    print(len(decimals))

run()
