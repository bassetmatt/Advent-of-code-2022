import numpy as np
with open('input') as f:
    A = np.array([[y for y in x] for x in f.read().splitlines()], dtype=int)
    B, S = np.zeros_like(A), np.ones_like(A)
    for i,j in np.ndindex(A.shape) :
        directions = [np.flip(A[i,:j]), A[i,j+1:], np.flip(A[:i,j]), A[i+1:,j]]
        B[i,j] = i in [0,A.shape[0]-1] or j in [0,A.shape[1]-1] or A[i,j] > min([max(d) for d in directions])
        for d in directions :
            s = 0
            for x in d :
                s += x <= A[i,j]
                if x == A[i,j]: break
            S[i,j] *= s
print(f"Visible Count : {np.sum(B)}\nBest scenic score : {np.max(S)}")