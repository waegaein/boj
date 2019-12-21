import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return int(f.readlines()[0].strip())


def move_hanoi_tower(n, from_tower, to_tower, spare_tower, moves):
    if n == 0:
        return moves

    moves = move_hanoi_tower(n-1, from_tower, spare_tower, to_tower, moves)
    moves.append(f'{from_tower} {to_tower}')
    moves = move_hanoi_tower(n-1, spare_tower, to_tower, from_tower, moves)

    return moves


def main():
    moves = move_hanoi_tower(parse_input(), 1, 3, 2, [])

    print(len(moves))
    for move in moves:
        print(move)

main()
