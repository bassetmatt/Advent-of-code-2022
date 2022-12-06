import re
overlaps = [0, 0]
with open('input') as f:
    for r in ( [int(x) for x in re.search("(\d+)-(\d+),(\d+)-(\d+)",l).groups()] for l in f.read().splitlines() ) : 
        r1, r2 = set(range(r[0], r[1] + 1)), set(range(r[2], r[3] + 1))
        overlaps[0] += r1.issubset(r2) or r1.issuperset(r2)
        overlaps[1] += not r1.isdisjoint(r2)
print(f"Ranges overlap part 1: {overlaps[0]}\nRanges overlap part 2: {overlaps[1]}")