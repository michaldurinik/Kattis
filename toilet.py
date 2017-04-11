#https://open.kattis.com/problems/toilet
from sys import stdin

seq = stdin.readline().strip()
seq = list(seq)
start = seq.pop(0)

u = 0
d = 0
p = 0
          
if start == "U" and seq[0] == "U":
    d += 1

if start == "U" and seq[0] == "D":
    u += 2
    d += 1
    p += 1
    
if start == "D" and seq[0] == "D":
    u += 1
    
if start == "D" and seq[0] == "U":
    u += 1
    d += 2
    p += 1

j = seq[0]

if len(seq) > 1: 
    for i in seq[1:]:
        if i == "D":    #only if own is Down (previous always Up), we put down, then up, 2x
            u += 2 
        else:
            d += 2      #if own is Up and we need to leave it down, it's +2
        if i != j:      #only if they different they change and leave it, +1
            p += 1
            j = i

print(str(u) + "\n" + str(d) + "\n" + str(p))