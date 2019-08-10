import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    raw = [line.strip() for line in f.readlines()[1:]]

    size_files = tuple(int(size_file) for size_file in raw[0].split())
    size_cluster = int(raw[1])

    return size_files, size_cluster

def run():
    size_files, size_cluster = parse_input()
    count = 0
    for size_file in size_files:
        if size_file > 0:
            if size_file % size_cluster == 0:
                count += (size_file // size_cluster)
            else:
                count += (size_file // size_cluster) + 1

    print(count * size_cluster)

run()
