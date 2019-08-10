import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return int(f.read().strip())

def is_lucky(ate_index, mid):
    return ate_index - mid < 100

def run():
    ate_index = parse_input()
    lucky_count = 0

    for mid in range(100):
        if is_lucky(ate_index, mid):
            lucky_count += 1

    print(lucky_count)

    return

run()
