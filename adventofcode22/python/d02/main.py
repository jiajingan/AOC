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
    'Z':3,
    'A':1,
    'B':2,
    'C':3
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
totalScorePart2 = 0
for i in lines:
    # 0 is opponent, 1 is me
    if(i[0] == loses_to[convert[i[1]]]):
        #win
        totalScore += RPS[i[1]] + 6
    if(convert[i[1]] == loses_to[i[0]]):
        #lose
        totalScore += RPS[i[1]] + 0
    if(i[0] == convert[i[1]]):
        totalScore += RPS[i[1]] + 3
        #tie
    
    # part 2 
    # X means lose, Y = draw, Z = win
    if(i[1]=="Y"):
    # 0 is opponent, 1 is me
        #draw
        totalScorePart2 += RPS[i[0]] + 3
    if(i[1]=="X"):
        #lose
        
        #loseto get win pick
        losePick = loses_to[i[0]]
        # print(i[0])
        # print("me:"+losePick)
        totalScorePart2 += RPS[losePick] + 0
    if(i[1]=="Z"):
        #win
        winPick = loses_to[loses_to[i[0]]]
        # print(i[0])
        # print("me:"+winPick)
        totalScorePart2 += RPS[winPick] + 6
print(totalScore)
print(totalScorePart2)
# print(lines)