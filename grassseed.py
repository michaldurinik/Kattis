#https://open.kattis.com/problems/grassseed
from sys import stdin
cost = float(stdin.readline().strip())
_ = stdin.readline()

total = 0.0
for line in stdin:
    line = line.strip().split()
    total += cost * float(line[0]) * float(line[1])
    
print("{:.7f}".format(total))
