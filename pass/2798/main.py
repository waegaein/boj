import sys

def parse_input():
    # with open('test.txt', 'r') as f:
    f = sys.stdin
    raw = [[int(c) for c in line.split()] for line in f.read().splitlines()]

    m = raw[0][1]
    num_cards = raw[0][0]
    cards = raw[1]

    return m, num_cards, cards

def main():
    m, num_cards, cards = parse_input()
    card_sum_max_so_far = 0
    for i in range(num_cards - 2):
        card_i = cards[i]

        for j in range(i + 1, num_cards - 1):
            card_j = cards[j]

            for k in range(j + 1, num_cards):
                card_k = cards[k]
                card_sum = card_i + card_j + card_k

                if card_sum > m:
                    continue

                if card_sum == m:
                    return card_sum

                if card_sum_max_so_far < card_sum < m:
                    card_sum_max_so_far = card_sum

    return card_sum_max_so_far

print(main())
