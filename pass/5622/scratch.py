import sys

def parse_input():
    input = sys.stdin
    # input = open('test.txt', 'r')

    return input.readline().replace('\n', '')

def get_number(character):
    alphabets = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    index = alphabets.index(character)
    if index < 3:
        return 2
    elif index < 6:
        return 3
    elif index < 9:
        return 4
    elif index < 12:
        return 5
    elif index < 15:
        return 6
    elif index < 19:
        return 7
    elif index < 22:
        return 8
    else:
        return 9

def calculate_cost(word):
    cost = 0
    for character in word:
        cost += get_number(character) + 1

    return cost

def run():
    print(calculate_cost(parse_input()))

    return

run()
