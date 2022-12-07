with open("input","r") as f :
    L = sorted([ sum([int(x) for x in elve.split('\n')]) for elve in f.read().split("\n\n")[:-1]], reverse=True)
print(f"Elve with max food {L[0]}, sum of 3 best elves' food : {sum(L[:3])}")