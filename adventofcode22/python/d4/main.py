import re
# parse file
fname = "adventofcode22/python/d4/input.txt"
with open(fname) as f:
    lines = []
    for line in f:
        a=line.strip('\n').split(',')
        lines.append(a)
total = 0
total1 = 0
for i in lines:
    #process numbers
    numlist = re.findall(r'\d+', i[0])
    numlist1 = re.findall(r'\d+', i[1])
    startnum = int(numlist[0])
    endnum = int(numlist[1])
    startnum1 = int(numlist1[0])
    endnum1 = int(numlist1[1])
    
    # checklist = []
    # checklist2 = []
    # for i in range (int(startnum),int(endnum)):
    #     checklist.append(str(i))
    # for i in range (int(startnum1),int(endnum1)):
    #     checklist2.append(str(i))
    # if (startnum1 in checklist and endnum1 in checklist):
    #     total+=1
    # elif (startnum in checklist2 and endnum in checklist2):
    #     total+=1
    
    #check conditions
    if((startnum<=startnum1) and (endnum>=endnum1)):
        total+=1
        total1+=1
    elif((startnum1<=startnum) and (endnum1>=endnum)):
        total +=1
        total1+=1
        
    #part 2 
    elif(startnum<=startnum1 and startnum1<=endnum):
        total1+=1
    elif(startnum1<=startnum and startnum<=endnum1):
        total1+=1
    
print(total)
print(total1)