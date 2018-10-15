#https://open.kattis.com/problems/numberfun
from sys import stdin

def op(x, y):
    return [x+y, x-y, x*y, x/y]

_ = stdin.readline()
for line in stdin:
    x, y, z  = [float(x) for x in line.strip().split()]
    if z in op(x, y)  or y in op(x, z) or x in op(y, z):
        print("Possible")
    else:
        print("Impossible")
