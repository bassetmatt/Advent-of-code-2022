import re
import numpy as np
import itertools
R,L,U,D = (1,0), (-1,0), (0,1), (0,-1)

def getMove(s:str) :
    n = int(s[2:])
    match s[0]:
        case 'R' :
            return R, n
        case 'L' :
            return L, n
        case 'U' :
            return U, n
        case 'D' :
            return D, n
H = np.array([0,0],dtype=int)
T = np.array([0,0],dtype=int)
visitedT = [T]
def followingH(H,T) :
    if np.linalg.norm(H-T) <= np.sqrt(2) :
        return T, 0
    elif 0 in H-T :
        return (H+T)/2, (H-T)/2
    else :
        move = np.sign(H-T)*np.ceil(np.abs(H-T)/2)
        return T + move, move

rope = np.zeros((10,2), dtype=int)
visited = [[] for i in range(10)]
with open('input') as f:
    X = f.read().splitlines()
    commands = [getMove(x) for x in X]
    for c in commands :
        for step in range(c[1]) :
            rope[0] += c[0]
            for i in range(9) :
                rope[i+1], _ = followingH(rope[i], rope[i+1])
            rope = np.array(rope,dtype=int)
            #print(f"T, move = {str(T), str(move)}")
            for i in range(10) :
                visited[i].append(rope[i])

#print(visitedT)
hashable = [[(x[0],x[1]) for x in visited[i]]for i in range(10)]
print(len(set(hashable[1])))
print(len(set(hashable[-1])))