#https://open.kattis.com/problems/karte
from sys import stdin

seen = set()
counter = {"P":13, "K":13, "H":13, "T":13}
s = stdin.readline().strip()
found = False

for i in range(0, len(s), 3):
    if s[i:i+3] in seen:
        found = True
        break
    else:
        seen.add(s[i:i+3])
        counter[s[i]] -= 1

if found:
    print("GRESKA")
else:
    print(counter["P"], counter["K"], counter["H"], counter["T"]) 
