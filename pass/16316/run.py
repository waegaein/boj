import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return f.readlines()[1].strip().split()

def run():
    words = parse_input()
    for i in range(len(words)):
        if words[i].isdigit() and int(words[i]) != i + 1:
            print('something is fishy')
            return

    print('makes sense')
    return

run()
