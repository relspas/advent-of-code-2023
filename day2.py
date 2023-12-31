import re

#Game 1: 4 red, 8 green; 8 green, 6 red; 13 red, 8 green; 2 blue, 4 red, 4 green

def part1():
    restrict = {"red":12,"green":13,"blue":14}
    #12 red cubes, 13 green cubes, and 14 blue cubes
    sum = 0
    with open("day2_input.txt") as f:
        for line in f:
            out = re.search("^Game (\d+):(.*)$",line)
            gameNum = int(out[1])
            rounds = out[2]
            rounds = rounds.split(";")
            flag = False
            for round in rounds:
                mixes = round.split(",")
                for mix in mixes:
                    out = re.search("(\d+) (green|red|blue)",mix)
                    cnt = out[1]
                    color = out[2]
                    if int(cnt) > restrict[color]:
                        flag = True
                        break
                if flag:
                    break
            if not flag:
                sum += gameNum
    return sum

def part2():
    sum = 0
    with open("day2_input.txt") as f:
        for line in f:
            out = re.search("^Game \d+:(.*)$", line)
            rounds = out[1]
            minAmt = {"green":0,"red":0,"blue":0}
            rounds = rounds.split(";")
            for round in rounds:
                mixes = round.split(",")
                for mix in mixes:
                    out = re.search("(\d+) (green|red|blue)",mix)
                    cnt = int(out[1])
                    color = out[2]
                    if cnt > minAmt[color]:
                        minAmt[color] = cnt
            power = minAmt["green"]*minAmt["red"]*minAmt["blue"]
            sum += power
    return sum

print(part1())
print(part2())