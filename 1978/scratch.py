import sys

def parse_input():
    infile = sys.stdin
#    infile = open('test.txt', 'r')

    num_input = int(infile.readline())
    input_line = infile.readline().split(' ')
    
    res = list()
    for i in input_line:
        res.append(int(i))

    return res

def is_prime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def run():
    input = parse_input()
    count = 0
    
    for i in input:
        if is_prime(i):
            count += 1

    print(count)

    return

run()
