import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return tuple(tuple(int(num) for num in line.strip().split()) for line in f.readlines()[1:])

def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def get_circumcenter(ax, ay, bx, by, cx, cy):
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    box_a = (ax ** 2 + ay ** 2)
    box_b = (bx ** 2 + by ** 2)
    box_c = (cx ** 2 + cy ** 2)

    ux = (box_a * (by - cy) + box_b * (cy - ay) + box_c * (ay - by)) / d
    uy = (box_a * (cx - bx) + box_b * (ax - cx) + box_c * (bx - ax)) / d

    radius = get_distance(ux, uy, ax, ay)

    return (ux, uy), radius

def get_max_mid_with_length(ax, ay, bx, by, cx, cy):
    len_ab = get_distance(ax, ay, bx, by)
    len_bc = get_distance(bx, by, cx, cy)
    len_ca = get_distance(cx, cy, ax, ay)
    mid_ab = ((ax + bx) / 2, (ay + by) / 2)
    mid_bc = ((bx + cx) / 2, (by + cy) / 2)
    mid_ca = ((cx + ax) / 2, (cy + ay) / 2)

    if len_ab > len_bc and len_ab > len_ca:
        return mid_ab, max(len_ab / 2, get_distance(*mid_ab, cx, cy))
    elif len_bc > len_ab and len_bc > len_ca:
        return mid_bc, max(len_bc / 2, get_distance(*mid_bc, ax, ay))
    else:
        return mid_ca, max(len_ca / 2, get_distance(*mid_ca, bx, by))

def get_center_min_radius(test_case):
    circumcenter, circumradius = get_circumcenter(*test_case)
    max_mid, mid_length = get_max_mid_with_length(*test_case)

    if circumradius < mid_length:
        return circumcenter
    else:
        return max_mid

def run():
    test_cases = parse_input()
    count = 0
    for test_case in test_cases:
        count += 1
        x, y = get_center_min_radius(test_case)
        print(f'Case #{count}: {round(x, 2):.2f} {round(y, 2):.2f}')

run()
