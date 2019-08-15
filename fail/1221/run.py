import sys
import time

def parse_input():
    # f = sys.stdin
    with open('test.txt', 'r') as f:
        return [tuple(int(num) for num in line.split()) for line in f.read().strip().split('\n')[1:]]

def get_unique_points(points):

    return list(dict.fromkeys(points))

def get_distance_square(point_from, point_to):
    diff_x = point_from[0] - point_to[0]
    diff_y = point_from[1] - point_to[1]
    diff_z = point_from[2] - point_to[2]

    return diff_x * diff_x + diff_y * diff_y + diff_z * diff_z

def get_min_distance_with_num_pairs():
    distances = list()
    points = get_unique_points(parse_input())
    num_points = len(points)

    min_distance = None
    min_distance_num = None

    for i in range(num_points-1):
        for j in range(i+1, num_points):
            distance = get_distance_square(points[i], points[j])

            if min_distance is None or distance < min_distance:
                min_distance = distance
                min_distance_num = 1

            elif distance == min_distance:
                min_distance_num += 1

    print(min_distance)
    print(min_distance_num)

    return

get_min_distance_with_num_pairs()
