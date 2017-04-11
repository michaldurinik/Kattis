#https://open.kattis.com/problems/speedlimit
from sys import stdin

for line in stdin:
    line = int(line.strip())
    
    if line == -1:
        break
        
    hours = 0
    miles = 0
    i = 0    
    while i < line:
        m, h = [int(x) for x in stdin.readline().strip().split()]
        miles += m*(h-hours)
        hours = h
        i += 1

    print(miles, "miles")