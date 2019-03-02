import sys

def parse_input():
    input = sys.stdin
    # input = open('test.txt', 'r')
    splitted = input.readline().split()

    return (splitted[0], splitted[1])

def compare_sangsu(num1, num2):
    return max(int(num1[::-1]), int(num2[::-1]))

def run():
    print(compare_sangsu(*parse_input()))

run()
