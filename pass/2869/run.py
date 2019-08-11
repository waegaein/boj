import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return tuple(int(x) for x in f.readline().strip().split())

def get_days_required():
    climbing, sliding, distance = parse_input()

    climbing_per_day = climbing - sliding
    distance_exclude_last_day = distance - climbing

    full_days = distance_exclude_last_day // climbing_per_day
    if distance_exclude_last_day % climbing_per_day != 0:
        full_days += 1

    days = full_days + 1
    print(days)

    return

get_days_required()
