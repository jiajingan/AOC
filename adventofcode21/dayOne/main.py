# advent of code day1
fname = "/Users/jackiegan/PycharmProjects/adventofcode21/dayOne/input.txt"

countIncrease = 0
countBy3 = 0

with open(fname) as f:
    lines = []
    for line in f:
        lines.append(int(line))

for i in range(0, len(lines) - 1):
    if lines[i] < lines[i + 1]:
        countIncrease += 1

for i in range(0, len(lines) - 3):
    sumPrev = (lines[i] + lines[i + 1] + lines[i + 2])
    sumCurrent = (lines[i + 1] + lines[i + 2] + lines[i + 3])
    if sumPrev < sumCurrent:
        countBy3 += 1

print(countIncrease)
print(countBy3)
