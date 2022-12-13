import re
import numpy as np
import itertools

cycles = 0
RX = 1
values = []

interesting = [20 + 40*k for k in range(6)]
with open('input') as f:
    X = f.read().splitlines()
    for i,x in enumerate(X) :
        if "addx" in x :
            cycles += 1
            # print(f"{i:3d} : cycles : {cycles:3d}, RX : {RX:3d} ({x})")
            if cycles in interesting :
                #print(RX, cycles, RX*cycles)
                values.append(RX*cycles)
            val = int(x[5:])
            cycles +=1
            #print(f"{i:3d} : cycles : {cycles:3d}, RX : {RX:3d} ({x})")
            if cycles in interesting :
                values.append(RX*cycles)
            RX += val
        else :
            cycles += 1
            if cycles in interesting :
                values.append(RX*cycles)



def operation(RX,pixels, crt_pos) :
    if RX - 1 <= crt_pos[1] <= RX + 1:
        pixels[crt_pos[0]] += '#'
    else :
        pixels[crt_pos[0]] += '.'

RX = 1
cycles = 0
with open('input') as f:
    X = f.read().splitlines()
pixels = ["" for _ in range(6)]
for i,x in enumerate(X) :
    if "addx" in x :
        crt_pos = cycles//40, cycles%40
        cycles += 1
        operation(RX,pixels,crt_pos)
        crt_pos = cycles//40, cycles%40
        cycles +=1
        operation(RX,pixels,crt_pos)
        val = int(x[5:])
        RX += val
    else :
        crt_pos = cycles//40, cycles%40
        cycles += 1
        operation(RX,pixels,crt_pos)

for line in pixels:
    print(line)