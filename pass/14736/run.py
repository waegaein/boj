import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    raw = [tuple(int(x) for x in line.split()) for line in f.read().strip().split('\n')]
    k = raw[0][1]
    a = raw[0][2]
    competitors = raw[1:]

    return k, a, competitors

def get_drinking_time(to_drink, drink_per_second, time_drink, time_rest):
    time_drink_required = to_drink // drink_per_second
    num_whole_drink = time_drink_required // time_drink
    remaining_drink = time_drink_required % time_drink

    if remaining_drink == 0:
        return time_drink_required + ((num_whole_drink - 1) * time_rest)
    else:
        return time_drink_required + (num_whole_drink * time_rest)

def run():
    to_drink, drink_per_second, competitors = parse_input()
    print(min([get_drinking_time(to_drink, drink_per_second, *competitor) for competitor in competitors]))

run()
