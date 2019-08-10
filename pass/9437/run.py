import sys

def parse_input():
    f = sys.stdin
    # with open('test.txt', 'r') as f:
    return [(int(x) for x in line.split()) for line in f.read().strip().split('\n')[:-1]]

def build_sheets(total):
    sheets = list()

    half = total // 2
    for i in range(1, half+1):
        idx = (i - 1) // 2
        if len(sheets) < idx + 1:
            sheets.append([i])
        else:
            sheets[idx].append(i)

    fold = len(sheets) - 1
    for i in range(half+1, total+1):
        idx = fold - ((i - 1) // 2)
        sheets[idx].append(i)

    return sheets

def get_discarded_along(sheets, discard):
    for sheet in sheets:
        if discard in sheet:
            sheet.remove(discard)
            sheet.sort()
            return sheet

def run():
    inputs = parse_input()
    for total, discard in inputs:
        print(' '.join([str(x) for x in get_discarded_along(build_sheets(total), discard)]))

run()
