import sys

def parse_input():
    f = sys.stdin
    with open('test.txt', 'r') as f:
        raw = [tuple(int(x) for x in line.split()) for line in f.read().strip().split('\n')]
        return raw[0][1], raw[1:]

def get_groups(patches):
    res = list()

    for patch in patches:
        extend = list()
        for existing in res:
            extend.append(existing + [patch])
        res += extend
        res.append([patch])

    return res

def get_max_distance_square(group):
    max_value = 0
    max_idx_i = 0
    max_idx_j = 0
    for i in range()

def is_reachable(group, k):
    return get_max_distance_square(group) <= k * k
