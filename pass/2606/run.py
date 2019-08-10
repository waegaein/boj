import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [tuple(int(node) for node in line.split()) for line in f.read().strip().split('\n')[2:]]

def already_in(node, groups):
    for idx in range(len(groups)):
        group = groups[idx]
        if node in group:
            return idx
    return -1

def build_groups(inputs):
    groups = list()
    for pair in inputs:
        node_first = pair[0]
        node_second = pair[1]
        node_first_already_in = already_in(node_first, groups)
        node_second_already_in = already_in(node_second, groups)
        if node_first_already_in != -1 and node_second_already_in != -1:
            if node_first_already_in != node_second_already_in:
                idx_ahead = min(node_first_already_in, node_second_already_in)
                idx_trail = max(node_first_already_in, node_second_already_in)
                groups[idx_ahead] += groups.pop(idx_trail)
        elif node_first_already_in != -1 and node_second_already_in == -1:
            groups[node_first_already_in].append(node_second)
        elif node_first_already_in == -1 and node_second_already_in != -1:
            groups[node_second_already_in].append(node_first)
        else:
            groups.append([node_first, node_second])

    return groups

def run():
    groups = build_groups(parse_input())

    for group in groups:
        if 1 in group:
            print(len(group) - 1)

    return

run()
