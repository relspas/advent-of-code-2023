import re

def decode(line):
    return re.search("^Card[ ]+\d+:  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+) \|  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)  ?(\d+)",line)

def cntMatches(line):
    out = decode(line)
    s = set()
    for i in range(1,11):
        s.add(out[i])
    cnt = 0
    for i in range(25):
        if out[11+i] in s:
            cnt+=1
    return cnt

def part1():
    with open("day4_input.txt") as f:
        sum = 0
        for line in f:
            cnt = cntMatches(line)
            if cnt != 0:
                sum += 2**(cnt-1)
    return sum

def part2():
    with open("day4_input.txt") as f:
        d = {} #card number -> multiplity of card
        lines = []
        for line in f:
            lines+=[line.rstrip()]
        for i in range(len(lines)):
            d[i]=1
    with open("day4_input.txt") as f:
        for lineNum, line in enumerate(lines):
            cnt = cntMatches(line)
            # print(lineNum,cnt)
            for i in range(cnt):
                d[lineNum+i+1] += d[lineNum]
            lineNum += 1
        total = 0
        for k,v in d.items():
            total += v
        return total


print(part1())
print(part2())