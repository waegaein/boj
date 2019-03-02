import sys

def parse_input():
    input = sys.stdin
    # input = open('test2.txt', 'r')

    return input.read().replace('\n', '')

def mark_croatian(word):
    return word.replace('c=', '@') \
               .replace('c-', '@') \
               .replace('dz=', '@') \
               .replace('d-', '@') \
               .replace('lj', '@') \
               .replace('nj', '@') \
               .replace('s=', '@') \
               .replace('z=', '@')

def run():
    print(len(mark_croatian(parse_input())))

    return

run()
