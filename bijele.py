#https://open.kattis.com/problems/bijele
from sys import stdin

default = [1,1,2,2,2,8]
found = stdin.readline().strip().split()

result = [int(x) - int(y) for x, y in zip(default, found)]
print(" ".join([str(x) for x in result]))



