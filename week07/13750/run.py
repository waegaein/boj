import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [x for x in f.read().strip().split('\n')][1:]

def get_subsequences(full_sequence):
    subsequences = list()

    for x in full_sequence:
        extend = list()

        for existing in subsequences:
            extend.append(existing + [x])
        subsequences += extend

        subsequences.append([x])

    return subsequences

def is_zigzag(sequence):
    direction = ''
    previous = None
    for current in sequence:
        if previous is not None:
            if current > previous:
                if direction == 'asc':
                    return False
                else:
                    direction = 'asc'
            elif current < previous:
                if direction == 'desc':
                    return False
                else:
                    direction = 'desc'
            else:
                return False

        previous = current

    return True

def run():
    full_sequence = ''.join(parse_input())
    subsequences = sorted(get_subsequences(full_sequence), key=lambda x: len(x), reverse=True)

    for subsequence in subsequences:
        if is_zigzag(subsequence):
            print(len(subsequence))
            return

    return

run()
