import sys

def parse_input():
    # with open('test.txt', 'r') as f:
    f = sys.stdin
    return [[int(num) for num in line.split()] for line in f.read().splitlines()[1:]]

def is_smaller(person1, person2):
    return person1[0] < person2[0] and person1[1] < person2[1]

def main():
    people = parse_input()
    num_people = len(people)
    iter_people = list(range(num_people))

    for i in iter_people:
        rank = 1
        for j in iter_people[:i] + iter_people[i+1:]:
            if is_smaller(people[i], people[j]):
                rank += 1
        print(rank)

    return

main()
