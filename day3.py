import re

def part1():
    sum = 0
    grid = []
    with open("day3_input.txt") as f:
        for line in f:
            grid.append(line.rstrip())
    p = re.compile("[0-9]+")
    for i in range(len(grid)):
        line = grid[i]
        for m in p.finditer(line):
            # print(m.start(), m.group())
            beg = m.start()
            len_ = len(m.group())
            end = beg+len_-1
            #same line
            if beg > 0 and re.search("[^0-9\.]",line[beg-1]) or\
                end < len(line)-1 and re.search("[^0-9\.]",line[end+1]):
                sum += int(m.group())

            #line before
            elif i>0 and(
                beg > 0 and re.search("[^0-9\.]",grid[i-1][beg-1]) or\
                end < len(line)-1 and re.search("[^0-9\.]",grid[i-1][end+1]) or\
                re.search("[^0-9\.]",grid[i-1][beg:end+1])
            ):
                sum += int(m.group())

            #line after
            elif i<len(grid)-1 and(
                beg > 0 and re.search("[^0-9\.]",grid[i+1][beg-1]) or\
                end < len(line)-1 and re.search("[^0-9\.]",grid[i+1][end+1]) or\
                re.search("[^0-9\.]",grid[i+1][beg:end+1])
            ):
                sum += int(m.group())
    return sum

def getNumberFromIndex(line,idx):
    # .453.. get 453 from index 1, 2, or 3
    # known that digit at index is a number
    #go left
    left = 0
    for i in range(idx-1,-1,-1):
        if re.search("[0-9]",line[i]):
            left+=1
        else:
            break
    #go right
    right = 0
    for i in range(idx+1,len(line)):
        if re.search("[0-9]",line[i]):
            right+=1
        else:
            break
    # print(line[idx-left:idx+right+1])
    return [int(line[idx-left:idx+right+1])]

def part2():
    sum = 0
    grid = []
    with open("day3_input.txt") as f:
        for line in f:
            grid.append(line.rstrip())
    p = re.compile("\*")
    for i in range(1,len(grid)):
        line = grid[i]
        for m in p.finditer(line):
            partCnt = 0
            parts = []
            # print(m.start(), m.group())
            beg = m.start()
            len_ = len(m.group())

            #same line
            """
            for cases: .*0 and 0.*
            """
            if beg > 0 and re.search("[0-9]",line[beg-1]):
                partCnt += 1
                parts += getNumberFromIndex(line,beg-1)
            if beg < len(line)-1 and re.search("[0-9]",line[beg+1]):
                partCnt += 1
                parts += getNumberFromIndex(line,beg+1)

            #line before
            """
            line before and line after have special case for first if. There are seven permutations of parts 
            on a different line than *. They are:
            0.. .0. ..0 00. 0.0 .00 000
             *   *   *   *   *   *   *
                             ^only this one creates 2 gears, the rest only create 1. Check this first.
                             then the other 6 cases. 3 of the cases can be covered by the other 3.
            """
            if i>0 and beg > 0 and re.search("[0-9]",grid[i-1][beg-1]) and \
                beg < len(line)-1 and re.search("[0-9]",grid[i-1][beg+1]) and \
                re.search("[^0-9]",grid[i-1][beg]):
                partCnt += 2
                parts += getNumberFromIndex(grid[i-1],beg-1)
                parts += getNumberFromIndex(grid[i-1],beg+1)
            elif i>0 and beg > 0 and re.search("[0-9]",grid[i-1][beg-1]):
                partCnt += 1
                parts += getNumberFromIndex(grid[i-1],beg-1)
            elif i>0 and beg < len(line)-1 and re.search("[0-9]",grid[i-1][beg+1]):
                partCnt += 1
                parts += getNumberFromIndex(grid[i-1],beg+1)
            elif i>0 and re.search("[0-9]",grid[i-1][beg]):
                partCnt += 1
                parts += getNumberFromIndex(grid[i-1],beg)

            #line after
            if i<len(grid)-1 and beg > 0 and re.search("[0-9]",grid[i+1][beg-1]) and \
                beg < len(line)-1 and re.search("[0-9]",grid[i+1][beg+1]) and \
                re.search("[^0-9]",grid[i+1][beg]):
                partCnt += 2
                parts += getNumberFromIndex(grid[i+1],beg-1)
                parts += getNumberFromIndex(grid[i+1],beg+1)
            elif i<len(grid)-1 and beg > 0 and re.search("[0-9]",grid[i+1][beg-1]):
                partCnt += 1
                parts += getNumberFromIndex(grid[i+1],beg-1)
            elif i<len(grid)-1 and beg < len(line)-1 and re.search("[0-9]",grid[i+1][beg+1]):
                partCnt += 1
                parts += getNumberFromIndex(grid[i+1],beg+1)
            elif i<len(grid)-1 and re.search("[0-9]",grid[i+1][beg]):
                partCnt += 1
                parts += getNumberFromIndex(grid[i+1],beg)
            
            if partCnt == 2: #is gear
                sum += parts[0]*parts[1]

    return sum

print(part1())
print(part2())