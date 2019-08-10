import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [int(x) for x in f.read().strip()]

def run():
    input = parse_input()

    zoom = len(input)

    point_x = 0
    point_y = 0

    zoom_current = zoom
    while len(input) != 0:
        unit_move = 2 ** (zoom_current - 1)
        input_current = input[0]

        if 1 == input_current:
            point_x += unit_move
        elif 2 == input_current:
            point_y += unit_move
        elif 3 == input_current:
            point_x += unit_move
            point_y += unit_move
        else:
            pass

        zoom_current -= 1
        input = input[1:]

    print(' '.join([str(x) for x in[zoom, point_x, point_y]]))

run()
