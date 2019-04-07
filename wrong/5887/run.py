import sys
from math import sqrt

def parse_input():
    f = sys.stdin
    with open('test.txt', 'r') as f:
        return tuple(int(x) for x in f.readline().strip().split())

def get_posts(m, n):
    posts = list()
    for i in range(m + 1):
        for j in range(n + 1):
            posts.append((i, j))

    return posts

def is_perfect_square(num):
    return int(sqrt(num)) ** 2 == num

def is_proper_length_with_flat(post_from, post_to, min, max):
    length_square = (post_from[0] - post_to[0]) ** 2 + (post_from[1] - post_to[1]) ** 2
    if length_square < min ** 2:
        return False
    elif length_square > max ** 2:
        return False
    elif length_square == 1 or length_square == 2:
        return True
    elif is_perfect_square(length_square):
        return False
    elif length_square % 2 == 0 and is_perfect_square(length_square // 2):
        return False
    else:
        return True

def run():
    m, n, min, max, factor = parse_input()
    count_flat = 0
    posts = get_posts(m, n)
    for i in range(len(posts)):
        for j in range(i+1, len(posts)):
            if is_proper_length_with_flat(posts[i], posts[j], min, max):
                count_flat = (count_flat + 1) % factor

    print(count_flat)

run()
