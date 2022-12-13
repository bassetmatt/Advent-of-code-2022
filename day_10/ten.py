cycles, p1, RX, pixels = [0], [0], 1, ["" for _ in range(6)]
def doCycle(cycles,pixels,RX, p1) :
    pixels[cycles[0]//40] += '█' if 0 <= cycles[0]%40 - RX + 1 <= 2 else ' '
    cycles[0] += 1
    p1[0] += RX*cycles[0] if ((cycles[0] - 20) % 40 == 0) else 0
with open('input') as f:
    for x in f.read().splitlines() :
        doCycle(cycles,pixels,RX,p1)
        if "addx" in x :
            doCycle(cycles,pixels,RX,p1)
            RX += int(x[5:])
print(f"Signal strenght: {p1}{chr(10)}Screen display :{chr(10)}{chr(10).join(pixels)}")