#https://open.kattis.com/problems/sibice
from sys import stdin
_, width, length = stdin.readline().strip().split()
hypotenuse = (int(width)**2 + int(length)**2) **0.5

for line in stdin:
    line = int(line.strip())
    if line <= hypotenuse:
        print("DA")
    else:
        print("NE")
