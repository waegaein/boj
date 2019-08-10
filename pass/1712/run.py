import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return tuple(int(x) for x in f.readline().strip().split())

def get_BEP():
    fixed_cost, variable_cost, price = parse_input()

    if price <= variable_cost:
        print(-1)
    else:
        print(fixed_cost // (price - variable_cost) + 1)

    return

get_BEP()
