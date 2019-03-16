import sys

def is_valid_line(line):
    return line != 'START' \
           and line != 'END' \
           and line != 'ENDOFINPUT' \
           and line != ''

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [line for line in f.read().split('\n') \
            if is_valid_line(line)]

def decypher(character):
    ascii = ord(character)
    if character in 'ABCDE':
        return chr(ord(character) + 21)
    else:
        return chr(ord(character) - 5)

def run():
    input = parse_input()
    decyphered_list = list()
    for line in input:
        decyphered_line = ''
        for character in line:
            if character.isalpha():
                decyphered_line += decypher(character)
            else:
                decyphered_line += character
        decyphered_list.append(decyphered_line)
    for line in decyphered_list:
        print(line)

run()
