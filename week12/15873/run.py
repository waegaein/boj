import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return f.read().strip()

def split_num_string(num_string):
    if 2 == num_string.count('0'):
        return 20
    elif 1 == num_string.count('0'):
        if num_string[1] == '0':
            return 10 + int(num_string[2])
        else:
            return int(num_string[0]) + 10
    else:
        return int(num_string[0]) + int(num_string[1])

def run():
    input_raw = parse_input()
    print(split_num_string(input_raw))

    return

run()
