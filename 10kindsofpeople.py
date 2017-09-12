#https://open.kattis.com/problems/10kindsofpeople
from sys import stdin
x, y = stdin.readline().strip().split()
x, y = int(x), int(y)

lst = []
for i in range(x):
    lst.append(stdin.readline().strip())

no_tests = int(stdin.readline().strip())

for line in stdin:
    line = [int(x) for x in line.strip().split()]
    print(line)
