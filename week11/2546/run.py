import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    raw = [[int(num) for num in line.strip().split()] for line in f.readlines() if len(line.strip()) > 0][1:]

    res = list()
    i = 0
    while i < len(raw):
        res.append([raw[i+1]] + [raw[i+2]])
        i += 3

    return res

def count_eligible(c_students, e_students):
    c_average = sum(c_students) / len(c_students)
    e_average = sum(e_students) / len(e_students)
    count = 0

    for c_student in c_students:
        if c_student < c_average and c_student > e_average:
            count += 1

    return count

def run():
    test_cases = parse_input()

    for test_case in test_cases:
        print(count_eligible(*test_case))

    return

run()
