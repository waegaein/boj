import sys

def parse_input():
    f = sys.stdin
    with open('test.txt', 'r') as f:
        return [line.strip() for line in f.readlines()][1]

def is_valid_for_pre_sequence(pre_sequence, current_sequence):
    current_sequence_length = len(current_sequence)

    while len(pre_sequence) > current_sequence_length:
        if pre_sequence[-current_sequence_length:] == current_sequence:
            pre_sequence = pre_sequence[:-current_sequence_length]
        else:
            return False

    if pre_sequence in current_sequence:
        if pre_sequence != current_sequence[-len(pre_sequence):]:
            return False
    else:
        return False

    return True

def is_valid_for_post_sequence(post_sequence, current_sequence):
    current_sequence_length = len(current_sequence)

    while len(post_sequence) > current_sequence_length:
        if post_sequence[:current_sequence_length] == current_sequence:
            post_sequence = post_sequence[current_sequence_length:]
        else:
            return False

    if post_sequence in current_sequence:
        if post_sequence != current_sequence[:len(post_sequence)]:
            return False
    else:
        return False

    return True

def is_valid_partial_sequence(index_from, index_to, full_sequence):
    current_sequence = full_sequence[index_from:index_to]

    pre_sequence = full_sequence[:index_from]
    post_sequence = full_sequence[index_to:]

    if not is_valid_for_pre_sequence(pre_sequence, current_sequence):
        return False

    if not is_valid_for_post_sequence(post_sequence, current_sequence):
        return False

    return True

def run():
    full_sequence = parse_input()
    full_sequence_length = len(full_sequence)

    partial_sequence_length = full_sequence_length

    for i in range(full_sequence_length-1):
        for j in range(1, full_sequence_length):
            current_length = j - i
            if current_length < partial_sequence_length:
                if is_valid_partial_sequence(i, j, full_sequence):
                    partial_sequence_length = current_length

    print(partial_sequence_length)

    return

run()
