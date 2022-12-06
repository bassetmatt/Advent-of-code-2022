start_packet, start_msg = 0, 0
with open('input') as f:
    x = f.read().splitlines()[0]
    for i,_ in enumerate(x) :
        start_packet += i +  4 if (start_packet == 0 and len(set(x[i:i +  4])) ==  4) else 0
        start_msg    += i + 14 if (start_msg    == 0 and len(set(x[i:i + 14])) == 14) else 0
print(f"Start of packet  : {start_packet}\nStart of message : {start_msg}")