import re

def part1():
    with open("day5_input_example.txt") as file:
        lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    seeds = lines[0].split()
    seeds = seeds[1:]
    seeds = [int(seed) for seed in seeds]
    print("seeds",seeds)

    maps = []
    for i in range(1,len(lines)):
        out1 = re.search("^(.* map:)$",lines[i])
        out2 = re.search("^(\d+) (\d+) (\d+)$", lines[i])
        if not out1 and not out2:
            continue
        elif not out2:
            maps.append([])
        else:
            maps[-1].append([int(out2[1]),int(out2[2])-int(out2[1])])
    for m in maps:
        m.sort(key=lambda a:a[0])
    print("maps",maps)

    final_vals = []
    trace = []
    for seed in [seeds[3]]:
        currVal = seed
        trace.append([])
        for m in maps:
            added = 0
            for i in range(len(m)):
                row = m[i]
                # print(len(m),seed,added,row[0],i)
                if currVal > row[0]:
                    added = row[1]
                    trace[-1].append(i)
            # print("added:",currVal,added,currVal+added)
            currVal+=added
        
        final_vals.append(currVal)
    # print(trace,final_vals)
    return min(final_vals)

print(part1())