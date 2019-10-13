import sys
from decimal import Decimal, ROUND_HALF_UP

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    total, cut = tuple(int(num) for num in lines[0].split())
    scores = [Decimal(line) for line in lines[1:]]

    return total, cut, scores

def get_cut_average(total, cut, scores):
    numerator = sum(scores[cut:total-cut])
    denominator = total - 2 * cut

    return numerator / denominator

def get_moderated_average(total, cut, scores):
    numerator = scores[cut] * cut + sum(scores[cut:total-cut]) + scores[total-cut-1] * cut

    return numerator / total

def get_averages():
    total, cut, scores = parse_input()

    scores_ascending = sorted(scores)

    print(f'{get_cut_average(total, cut, scores_ascending).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)}')
    print(f'{get_moderated_average(total, cut, scores_ascending).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)}')

    return

get_averages()
