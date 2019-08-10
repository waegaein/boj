import sys

def parse_input():
    f = sys.stdin
    with open('test.txt', 'r') as f:
        return tuple(tuple(int(num) for num in line.strip().split()) for line in f.readlines()[1:])

def predict(total, ours, theirs, win_threshold):
    ours_predicted = (total - (ours + theirs)) * 0.5
    ours_probability = (ours + ours_predicted) / total
    win_probability = win_threshold / 100
    if ours_probability > win_probability:
        print('GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!')
    elif 1.0 - ours_probability > win_probability:
        print('RECOUNT!')
    else:
        print('PATIENCE, EVERYONE!')

    return

def run():
    tests = parse_input()
    for test in tests:
        predict(*test)

    return

run()
