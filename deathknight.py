#https://open.kattis.com/problems/deathknight
from sys import stdin
total = 0
_ = stdin.readline()
for line in stdin:
    if "CD" not in line:
        total +=1

print(total)
