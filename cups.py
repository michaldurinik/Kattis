#https://open.kattis.com/problems/cups
from sys import stdin
_ = stdin.readline()

color_dict = {}
for pair in stdin:
    pair = pair.strip().split()
    if pair[0].isdigit():
        color_dict[int(pair[0])//2] = pair[1]
    else:
        color_dict[int(pair[1])] = pair[0]
        
for radius, color in sorted(color_dict.items()):
    print(color)