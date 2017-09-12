#https://open.kattis.com/problems/planina
from sys import stdin

points = 2
n = int(stdin.readline().strip())

for i in range(n):
    points = points * 2 - 1

print(points**2)
