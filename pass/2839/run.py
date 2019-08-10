import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return int(f.readline().strip())

def get_num_bags_five_kilos(total_amount):
    num_bags_five_kilos = total_amount // 5

    while (total_amount - 5 * num_bags_five_kilos) % 3 != 0 and num_bags_five_kilos > 0:
        num_bags_five_kilos -= 1

    return num_bags_five_kilos

def get_min_bags_required():
    total_amount = parse_input()
    num_bags_five_kilos = get_num_bags_five_kilos(total_amount)
    num_bags_three_kilos = (total_amount - 5 * num_bags_five_kilos) // 3
    remaining_amount = (total_amount - 5 * num_bags_five_kilos) % 3

    if remaining_amount != 0:
        print(-1)
    else:
        print(num_bags_five_kilos + num_bags_three_kilos)

    return

get_min_bags_required()
