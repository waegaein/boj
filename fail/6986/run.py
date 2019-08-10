import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    lines = f.read().strip().split('\n')

    num_grade_drop_end = int(lines[0].split()[1])
    grades = [float(x) for x in lines[1:]]

    return num_grade_drop_end, grades

def get_average_dropped(num_grade_drop_end, grades_sorted):
    grades_dropped = grades_sorted[num_grade_drop_end : -num_grade_drop_end]
    return sum(grades_dropped) / (len(grades_sorted) - 2 * num_grade_drop_end)

def get_average_compromised(num_grade_drop_end, grades_sorted):
    left_end = grades_sorted[num_grade_drop_end]
    right_end = grades_sorted[-(num_grade_drop_end+1)]
    grades_compromised = [left_end] * num_grade_drop_end \
                         + grades_sorted[num_grade_drop_end : -num_grade_drop_end] \
                         + [right_end] * num_grade_drop_end
    return sum(grades_compromised) / len(grades_sorted)

def round_with_trailing_zeros(raw, precision):
    rounded = str(round(raw, precision))
    if '.' in rounded:
        while len(rounded.split('.')[1]) < precision:
            rounded += '0'
    else:
        rounded += '.00'
    return rounded

def run():
    num_grade_drop_end, grades = parse_input()
    grades_sorted = sorted(grades)
    print(round_with_trailing_zeros(get_average_dropped(num_grade_drop_end, grades_sorted), 2))
    print(round_with_trailing_zeros(get_average_compromised(num_grade_drop_end, grades_sorted), 2))

run()
