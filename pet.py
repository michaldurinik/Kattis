#https://open.kattis.com/problems/pet
from sys import stdin

a = []
for line in stdin: 
    lst = [int(x) for x in line.strip().split()]
    a.append(sum(lst))
    
per, pts = 0, a[0]     
for idx, num in enumerate(a):
    if num > pts:
        per = idx
        pts = num

print(per+1, pts)