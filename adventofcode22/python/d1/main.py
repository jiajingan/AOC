# AOC day 1 in python

# parse file
fname = "adventofcode22/input.txt"
with open(fname) as f:
    lines = []
    for line in f:
        lines.append(line.strip("\n"))
        
maxCalories = 0
currCal = 0
for i in lines:
    if (i != ''):
        currCal += int(i)
    else:
        currCal = 0
    
    if(maxCalories<currCal):
        maxCalories = currCal

print(maxCalories)
#O(n) in time complexity
#O(1) in space complexity