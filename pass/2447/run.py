import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return int(f.readlines()[0].strip())

def get_triple_merged(item):
    merged = list()
    for i in range(len(item)):
        merged.append(''.join([item[i] for x in range(3)]))
    return merged

def get_mid_merged(block, hole):
    merged = list()
    for i in range(len(block)):
        merged.append(''.join([block[i], hole[i], block[i]]))
    return merged

def get_stars(n):
    if n == 1:
        return [['*'], [' ']]

    block, hole = get_stars(n // 3)

    block_triple_merged = get_triple_merged(block)
    mid_triple_merged = get_mid_merged(block, hole)
    hole_triple_merged = get_triple_merged(hole)

    block_next = (
        block_triple_merged
        + mid_triple_merged
        + block_triple_merged
    )
    hole_next = (
        hole_triple_merged
        + hole_triple_merged
        + hole_triple_merged
    )
    return block_next, hole_next

def main():
    n = parse_input()
    for line in get_stars(n)[0]:
        print(line)

    return

main()
