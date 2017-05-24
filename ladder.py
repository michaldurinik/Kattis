#https://open.kattis.com/problems/ladder
from sys import stdin
from math import sin, radians, ceil
height, angle = [int(n) for n in stdin.readline().strip().split()]

print(ceil(height / sin(radians(angle)))) # *sin(90degrees) = 1 
