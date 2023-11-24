import sys
sys.path.append("adventofcode15/python/")

import input

# part 1 
def presentDim (length: int, width: int, height: int) -> int:
    temp = [length,width,height]
    temp.sort()
    slack = temp[0] * temp[1]
    total = (2*length*width)+(2*width*height)+(2*height*length)+slack
    return total

def part1(data):
    ans = 0
    for i in data:
        num = i.split("x")
        ans += presentDim(int(num[0]),int(num[1]),int(num[2]))
    return ans

# part 2
def ribbon (length: int, width: int, height: int) -> int:
    temp = [length,width,height]
    temp.sort()
    slack = temp[0] + temp[1] + temp[0] + temp[1]
    rib = slack + (length*width*height)
    return rib
    
def part2(data):
    ans = 0
    for i in data:
        num = i.split("x")
        ans += ribbon(int(num[0]),int(num[1]),int(num[2]))
    return ans

if __name__ == "__main__":
    fname =  "adventofcode15/input/d2/input.txt"
    data = input.inputFile(fname, False)
    print(f'part1:{part1(data)}')
    print(f'part2:{part2(data)}')    