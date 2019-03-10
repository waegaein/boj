import sys

def parse_input():
    f = sys.stdin
    # f = open('test.txt', 'r')

    return [int(x) for x in f.readline() if x.isdigit()]

def get_state():
    state = None
    previous = None
    for note in parse_input():
        if previous is None:
            previous = note
        else:
            if note > previous:
                if state is None:
                    state = 'ascending'
                    previous = note
                elif state == 'descending':
                    return 'mixed'
                else:
                    previous = note
            else:
                if state is None:
                    state = 'descending'
                    previous = note
                elif state == 'ascending':
                    return 'mixed'
                else:
                    previous = note

    return state

print(get_state())
