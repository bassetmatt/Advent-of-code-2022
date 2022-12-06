getRef = lambda c: ord('a') if c.islower() else ord('A') - 26
priorities = [0, 0]

with open('input') as f:
    L = f.read().split('\n')[:-1]

for idx, sack in enumerate(L) :
    for x in sack[:len(sack)//2] : 
        if x in sack[len(sack)//2:] :
            priorities[0] += ord(x) - getRef(x) + 1
            break
    for x in sack:
        if (idx % 3 == 0 and x in L[idx+1] and x in L[idx+2]) :
            priorities[1] += ord(x) - getRef(x) + 1
            break
print(f"Prios part 1 : {priorities[0]}\nPrios part 2 : {priorities[1]}")