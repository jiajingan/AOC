# AOC day 1 in python

# parse file
fname = "adventofcode22/python/d1/input.txt"
with open(fname) as f:
    lines = []
    for line in f:
        lines.append(line.strip("\n"))

# part 1
maxCalories = 0
currCal = 0
maxThree = []
counter = 0
for i in lines:
    if (i != ''):
        currCal += int(i)
    else:
        currCal = 0
    
    if(maxCalories<currCal):
        maxCalories = currCal
    
    #part 2
    maxThree.append(currCal)
    if(len(maxThree)>= 4):
        maxThree.remove(min(maxThree))
    

print(maxCalories)
print(maxThree)
print(sum(maxThree))
#part 1 
#O(n) in time complexity
#O(1) in space complexity

#part 2 
#O(n) in time complexity
#O(n) in space complexity, list