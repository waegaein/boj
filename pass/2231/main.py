import sys

def parse_input():
    # with open('test.txt', 'r') as f:
    f = sys.stdin
    return int(f.readline().strip())

def get_constructed(num):
    return sum(int(c) for c in str(num)) + num

def get_base_aux(num, base):
    if num < 18:
        return 1

    base_next = base * 10 + 9
    constructed_next = get_constructed(base_next)

    if constructed_next > num:
        return base
    else:
        return get_base_aux(num, base_next)

def get_base(num):
    return get_base_aux(num, 9)

def main():
    num = parse_input()
    base = get_base(num)
    for i in range(base, num):
        if get_constructed(i) == num:
            return i

    return 0

print(main())
