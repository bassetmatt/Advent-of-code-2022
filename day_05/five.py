import re
containers, box = [[[] for _ in range(9)] for _ in range(2)], "[\[ ](.)[\] ]"
with open('input','r') as f:
    for i, l in enumerate(f.read().splitlines()) :
        if i <= 8 : # init
            for j, a in enumerate(re.search(f"{box} {box} {box} {box} {box} {box} {box} {box} {box}",l).groups()) :
                containers[0][j] += [a] if a != " " else []
                containers[1][j] += [a] if a != " " else []
        if i >= 10 : # moving
            s = list(map(int,re.search("move (\d+) from (\d) to (\d)",l).groups()))
            containers[0][s[2]-1] = containers[0][s[1]-1][:s[0]][::-1] + containers[0][s[2]-1]
            containers[1][s[2]-1] = containers[1][s[1]-1][:s[0]]       + containers[1][s[2]-1]
            containers[0][s[1]-1], containers[1][s[1]-1] = containers[0][s[1]-1][s[0]:], containers[1][s[1]-1][s[0]:]
print("".join(map(lambda x : x[0], containers[0]))+'\n'+"".join(map(lambda x : x[0], containers[1])))