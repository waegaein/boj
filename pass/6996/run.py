import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return tuple(tuple(line.strip().split()) for line in f.readlines()[1:])

def get_occurrences(word):
    occurrences = dict()
    for character in word:
        if character in occurrences.keys():
            occurrences[character] += 1
        else:
            occurrences[character] = 1

    return occurrences

def are_anagrams(word1, word2):
    return get_occurrences(word1) == get_occurrences(word2)

def run():
    pairs = parse_input()
    for word1, word2 in pairs:
        if are_anagrams(word1, word2):
            print("{0} & {1} are anagrams.".format(word1, word2))
        else:
            print("{0} & {1} are NOT anagrams.".format(word1, word2))

    return

run()
