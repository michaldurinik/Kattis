#https://open.kattis.com/problems/cetvrta
from sys import stdin
a=[]
b=[]
for line in stdin:
    x, y = line.strip().split()
    a.append(x)
    b.append(y)

lst = [str(x) for x in a if a.count(x) % 2 != 0] + [str(y) for y in b if b.count(y) % 2 != 0]
print(" ".join(lst))
    