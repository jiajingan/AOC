# AOC day 3 in python
# part 2
fname = "adventofcode22/python/d3/input.txt"
with open(fname) as f:
    lines = []
    for line in f:
        a=line.strip("\n")
        lines.append(a)
total = 0  
i=0
# print(len(lines))   
# print(i)
while(not(len(lines)==i)):
    # print(i)
    common_character = ''.join(set(lines[i]).intersection(lines[i+1]).intersection(lines[i+2]))
    print(common_character)   
    if(ord(common_character)>64 and ord(common_character)<91):
        # isupper
        total += ord(common_character)-38
    if(ord(common_character)>96 and ord(common_character)<123):
        # islower
        total += ord(common_character)-96
    i = i+3
print(total)


        