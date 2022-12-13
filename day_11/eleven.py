import math
isOld = lambda x,s : x if 'old' in s else int(s) 
def parseOperation(op:str) :
    symb = '+' if '+' in op else '*'
    l,r = op.split(symb)[0], op.split(symb)[1]
    return (lambda x: isOld(x,l) + isOld(x,r)) if symb == '+' else (lambda x: isOld(x,l) * isOld(x,r))
class Monke :
    def __init__(self, s:str) -> None:
        self.id = int(s[0][7])
        self.list1 = list(map(int,s[1][18:].split(', ')))
        self.list2 = list(self.list1)
        self.op = parseOperation(s[2][19:])
        self.mod = int(s[3][21:])
        self.test = lambda x: int(s[4][-1]) if x%self.mod == 0 else int(s[5][-1])
        self.look = [0,0]
with open('input') as f:
    monkeList:list[Monke] = [Monke(x.split('\n')) for x in f.read().split('\n\n')]
    lcm = math.lcm(*[m.mod for m in monkeList])
    for round in range(10000):
        for monke in monkeList :
            monke.look[0] += len(monke.list1) if round < 20 else 0
            monke.look[1] += len(monke.list2)
            for _ in range(len(monke.list1)) :
                item = math.floor(monke.op(monke.list1.pop(0))/3) % lcm
                monkeList[monke.test(item)].list1.append(item)
            for _ in range(len(monke.list2)) :
                item = monke.op(monke.list2.pop(0)) % lcm
                monkeList[monke.test(item)].list2.append(item)
looks = sorted([m.look[0] for m in monkeList]), sorted([m.look[1] for m in monkeList])
print(f"monkey business part 1 : {looks[0][-1]*looks[0][-2]}\nMonkey business part 2 : {looks[1][-1]*looks[1][-2]}")