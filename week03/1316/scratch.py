import sys

def parse_input():
    input = sys.stdin
    input.readline()
    res = list()
    for line in input.readlines():
        res.append(line[:-1])

    return res

def is_group_word(word):
    appeared = list()
    current = None
    for character in word:
        if current is None:
            appeared.append(character)
            current = character
        elif character != current and character in appeared:
            return False
        else:
            appeared.append(character)
            current = character

    return True

def run():
    inputs = parse_input()
    count = 0
    for input in inputs:
        if is_group_word(input):
            count += 1

    print(count)
    return

run()
