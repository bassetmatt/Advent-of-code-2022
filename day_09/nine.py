import numpy as np
dirs = {'R': (1,0), 'L' : (-1,0), 'U' : (0,1), 'D' :(0,-1)}
getMove = lambda H,T : 0 if np.linalg.norm(H-T) <= np.sqrt(2) else np.sign(H-T)*np.ceil(np.abs(H-T)/2).astype(int)
rope, visited = np.zeros((10,2), dtype=int), [[] for _ in range(9)]
with open('input') as f:
    for command in [(dirs[x[0]], int(x[2:])) for x in f.read().splitlines()] :
        for step in range(command[1]) :
            rope[0] += command[0]
            for i in range(9) :
                rope[i+1] += getMove(rope[i], rope[i+1])
                visited[i].append(rope[i+1].tobytes())
visitedCount = list(map(lambda x : len(set(x)), visited))
print(f"Number of states (p1) : {visitedCount[0]}\nNumber of states (p2) : {visitedCount[-1]}")