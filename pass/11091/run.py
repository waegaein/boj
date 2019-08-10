import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return tuple(line.strip() for line in f.readlines()[1:])

def is_pangram(sentence):
    lowered = ''.join([character.lower() for character in sentence if character.isalpha()])

    not_exist = ''
    for i in range(ord('a'), ord('z')+1):
        if chr(i) not in lowered:
            not_exist += chr(i)

    return len(not_exist) == 0, not_exist

def run():
    sentences = parse_input()
    for sentence in sentences:
        pangram, not_exist = is_pangram(sentence)
        if pangram:
            print('pangram')
        else:
            print(f'missing {not_exist}')

    return

run()
