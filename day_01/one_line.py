print("Elve with max food:", sorted([ sum([int(x) for x in elve.split('\n')]) for elve in open('input','r').read().split('\n\n')[:-1]], reverse=True)[0], "\nSum of 3 best elves' food :", sum(sorted([ sum([int(x) for x in elve.split('\n')]) for elve in open('input','r').read().split('\n\n')[:-1]], reverse=True)[:3]))