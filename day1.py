
def getNumFromLine(str_):
    first = ""
    last = ""
    for c in str_:
        if c.isdigit():
            first = c
            break
    for c in str_[::-1]:
        if c.isdigit():
            last = c
            break
    return int(first+last)

def getNumFromLine2(str_):
    first = ""
    last = ""
    first_idx = len(str_)#one longer than last idx for MAX behavior
    last_idx = -1

    for i,c in enumerate(str_):
        if c.isdigit():
            first = c
            first_idx = i
            break

    #find index of substrings, earliest index wins
    nums = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for num_i,num in enumerate(nums):
        loc = str_.find(num)
        if loc != -1 and loc < first_idx:
            first_idx = loc
            first = str(num_i)

    for i in range(len(str_)-1,-1,-1):
        c = str_[i]
        if c.isdigit():
            last = c
            last_idx = i
            break

    for num_i,num in enumerate(nums):
        loc = str_.rfind(num)
        if  loc > last_idx:
            last_idx = loc
            last = str(num_i)

    return int(first+last)

def part1():
    with open("day1_input.txt") as f:
        sum_ = 0
        for line in f:
            sum_ += getNumFromLine(line)
        return sum_

def part2():
    with open("day1_input.txt") as f:
        sum_ = 0
        cnt = 3
        for line in f:
            amt = getNumFromLine2(line.rstrip())
            sum_ += amt
        return sum_

print("part1",part1())
print("part2",part2())