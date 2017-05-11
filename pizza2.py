#https://open.kattis.com/problems/pizza2
from sys import stdin
from math import pi

line = stdin.readline().strip().split()
r1 = float(line[0])
r2 = float(line[1])

area = pi * r1**2
cheese = pi * (r1-r2)**2
crust = area - cheese
coverage = cheese/area*100

print("{:.6f}".format(coverage))