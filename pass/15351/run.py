import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return f.read().strip().split('\n')[1:]

def calculate_score(life):
    score = 0
    for character in life:
        if character.isalpha() and character.isupper():
            score += ord(character) - ord('A') + 1

    return score

def run():
    inputs = parse_input()
    for line in inputs:
        score = calculate_score(line)
        if score == 100:
            print('PERFECT LIFE')
        else:
            print(score)

run()
