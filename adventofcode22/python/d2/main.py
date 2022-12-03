# AOC day 2 in python

# parse file
fname = "adventofcode22/python/d2/input.txt"
with open(fname) as f:
    lines = []
    for line in f:
        lines.append(line.strip("\n").split())

RPS = {
    'X':1,
    'Y':2,
    'Z':3 
}
# https://davidamos.dev/revisiting-rock-paper-scissors-in-python/
"""
    suppose 
    Rock = A
    Paper = B
    Scissors = C
"""
loses_to = {
    "A": "C",
    "B": "A",
    "C": "B",
}

convert = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}
totalScore = 0
for i in lines:
    # 0 is opponent, 1 is me
    # print(loses_to[i[0]])
    if(i[0] == loses_to[convert[i[1]]]):
        #win
        totalScore += RPS[i[1]] + 6
    if(convert[i[1]] == loses_to[i[0]]):
        #lose
        totalScore += RPS[i[1]] + 0
    if(i[0] == convert[i[1]]):
        totalScore += RPS[i[1]] + 3
        #tie

print(totalScore)
# print(lines)