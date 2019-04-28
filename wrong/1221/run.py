import sys

def parse_input():
    f = sys.stdin
    with open('test.txt', 'r') as f:
        return [tuple(int(coordinate) for coordinate in line.strip().split()) for line in f.readlines()[1:]]

def get_distance_square(coordinates1, coordinates2):
    distance_square = 0
    for i in range(3):
        distance_square += (coordinates1[i] - coordinates2[i]) ** 2

    return distance_square

def get_unique_coordinates(coordinates):

    return list(set(coordinates))

def run():
    coordinates = get_unique_coordinates(parse_input())
    coordinates_length = len(coordinates)
    minimum_distance_square = None
    minimum_distance_square_count = 0

    for i in range(coordinates_length-1):
        for j in range(i+1, coordinates_length):
            distance_square = get_distance_square(coordinates[i], coordinates[j])
            if minimum_distance_square is None or distance_square < minimum_distance_square:
                minimum_distance_square = distance_square
                minimum_distance_square_count = 1
            elif distance_square == minimum_distance_square:
                minimum_distance_square_count += 1
            else:
                pass

    print(minimum_distance_square)
    print(minimum_distance_square_count)

    return

run()
