import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [[int(num) for num in line.strip().split()] for line in f.readlines()]

def is_match(preferences, num_preferences, index):
    preference_reference = set(preferences[0][:index])
    for i in range(1, num_preferences):
        if set(preferences[i][:index]) != preference_reference:
            return False

    return True

def get_match_index(num_songs, num_preferences, preferences):
    for i in range(1, num_songs):
        if is_match(preferences, num_preferences, i):
            return i

    return num_songs

def run():
    input_raw = parse_input()
    num_preferences = input_raw[0][0]
    num_songs = input_raw[0][1]
    preferences = input_raw[1:]

    match_index = get_match_index(num_songs, num_preferences, preferences)

    print(match_index)
    print(' '.join([str(num) for num in sorted(preferences[0][:match_index])]))

    return

run()
