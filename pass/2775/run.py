import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    f = f.read()
    linear = [int(line) for line in f.strip().split('\n')[1:]]
    return [linear[i*2:(i+1)*2] for i in range(len(linear) // 2)]

def get_residents(floor, suite):
    residents_map = list()
    for f in range(floor+1):
        per_floor = list()

        for s in range(suite):
            if s == 0:
                per_floor.append(1)
            elif f == 0:
                per_floor.append(s+1)
            else:
                per_floor.append(per_floor[s-1] + residents_map[f-1][s])

        residents_map.append(per_floor)

    return residents_map[floor][suite-1]

def main():
    cases = parse_input()

    for case in cases:
        print(get_residents(*case))

    return

main()
