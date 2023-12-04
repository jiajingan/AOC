# import sys
# sys.path.append("adventofcode15/python/")

import input
# from ..input import inputFile
fname =  "adventofcode15/input/d1/input.txt"

# part 1 
data = input.inputFile(fname, True)
# print(data)
def part1(data):
    floor = 0
    for i in data:
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1
    return floor
print(f'part1:{part1(data)}')


def part2(data):
    floor = 0
    pos = 0
    for i in data:
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1
        pos += 1
        if floor < 0:
            return pos    
print(f'part2:{part2(data)}')
