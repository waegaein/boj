import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    raw = [line.strip() for line in f.readlines()]

    pairs = list()
    i = 0
    while True:
        if raw[i] == 'E':
            break;
        pairs.append((raw[i], raw[i+1]))
        i += 2

    return pairs

def get_game_result(p1, p2):
    if p1 == p2:
        return 0
    elif (p1 == 'R' and p2 == 'S') \
         or (p1 == 'P' and p2 == 'R') \
         or (p1 == 'S' and p2 == 'P'):
        return 1
    else:
        return -1

def simulate_games(p1, p2):
    win_p1 = 0
    win_p2 = 0
    for i in range(len(p1)):
        game_result = get_game_result(p1[i], p2[i])
        if 1 == game_result:
            win_p1 += 1
        if -1 == game_result:
            win_p2 += 1

    print('P1: ' + str(win_p1))
    print('P2: ' + str(win_p2))

    return

def run():
    input_pairs = parse_input()
    for pair in input_pairs:
        simulate_games(*pair)

    return

run()
