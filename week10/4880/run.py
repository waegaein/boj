import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return tuple(tuple(int(num) for num in line.strip().split()) for line in f.readlines()[:-1])

def is_ap(sequence):
    difference = sequence[1] - sequence[0]
    for i in range(1, len(sequence)):
        if sequence[i] - sequence[i-1] != difference:
            return False

    return True

def get_next_ap(sequence):
    last = sequence[-1]
    difference = sequence[1] - sequence[0]

    return last + difference

def get_next_gp(sequence):
    last = sequence[-1]
    ratio = sequence[1] // sequence[0]

    return last * ratio

def run():
    sequences = parse_input()
    for sequence in sequences:
        if is_ap(sequence):
            print(f'AP {get_next_ap(sequence)}')
        else:
            print(f'GP {get_next_gp(sequence)}')

    return

run()
