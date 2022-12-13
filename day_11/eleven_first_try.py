import math
def parseOperation(op:str) :
    if '+' in op :
        symb = ' + '
    else :
        symb = ' * '
    op = op.split(symb)
    for i in range(len(op)) :
        if 'old' in op[i] :
            op[i] = 'o'
        else :
            op[i] = int(op[i])
    
    return op[0], symb[1], op[1]

class Monke :
    def __init__(self, s:str) -> None:
        self.id = int(s[0][7])
        self.list = list(map(int,s[1][18:].split(', ')))

        self.op = parseOperation(s[2][19:])
        self.test = int(s[3][21:])
        self.true = int(s[4][-1])
        self.false = int(s[5][-1])
        self.look = 0
    
    def applyOperation(self,old) :
        left  = old if self.op[0] == 'o' else self.op[0]
        right = old if self.op[2] == 'o' else self.op[2]
        if self.op[1] == '+' :
            return left+right
        else :
            return left*right
        
    def __str__(self) -> str:
        return f"Monke {self.id}\n" + \
               f"Items {self.list}\n" + \
               f"Operation {self.op}\n" + \
               f"Test {self.test}\n" + \
               f"True {self.true}, False {self.false}\n"

def printRound(m:Monke) :
    return f"Monke {m.id}\n" + \
            f"Items {m.list}\n"
    
with open('input') as f:
    X = f.read().split('\n\n')
    iteration = 0
    monkeList:list[Monke] = []
    for x in X:
        m = Monke(x.split('\n'))
        monkeList.append(m)
    value = math.lcm(*[m.test for m in monkeList])
    print(value)
    milestones = [1,20] + [1000*k for k in range(1,11)]
    res = []
    #print([m.id for m in monkeList])
    for iteration in range(10000):
        for monke in monkeList :
            for _ in range(len(monke.list)) :
                monke.look += 1
                it = monke.list.pop(0)
                it = monke.applyOperation(it) % value
                if it % monke.test == 0 :
                    monkeList[monke.true].list.append(it)
                else :
                    monkeList[monke.false].list.append(it)
        if iteration+1 in milestones :
            res.append([m.look for m in monkeList])

    l = sorted([m.look for m in monkeList],reverse=True)
    print(l)
    print(l[0]*l[1])
    for r in res :
        print(r)