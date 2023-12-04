
import input
import re
# from ..input import inputFile
fname =  "adventofcode23/input/d1/input.txt"

# part 1 
data = input.inputFile(fname, False)
# print(data)
def part1(data):
    ans = 0 
    for i in data:
        a = re.sub("[^0-9]", "", i)
        if (len(a) == 1):
            a = a[0] + a[0]
        elif(len(a)>1):
            a = a[0] + a[-1]
        ans += int(a)
        print(a)
    return ans


def part2(data):
    digits = ["one","two","three","four","five","six","seven","eight","nine"]
    nums = ["1","2","3","4","5","6","7","8","9"]
    ans = 0 
    # we can compare index 
    for i in data:
        numStrip = re.sub("[^0-9]", "", i)
        a = [i[j:j+3] for j in range(0,len(i),3)]
        b = [i[j:j+4] for j in range(0,len(i),4)]
        c = [i[j:j+5] for j in range(0,len(i),5)]
        counter = 0
        if ()
        print(a)

            
        
        # if (len(a) == 1):
        #     a = a[0] + a[0]
        # elif(len(a)>1):
        #     a = a[0] + a[-1]
        # ans += int(a)
        # print(a)
    return ans


if __name__ == "__main__":
    # print(f'part1:{part1(data)}')
    print(f'part2:{part2(data)}')