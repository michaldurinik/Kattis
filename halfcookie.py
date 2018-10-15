#https://open.kattis.com/problems/halfacookie
from sys import stdin
from math import sqrt, pi, sin, asin

for line in stdin:
    r, x, y = [float(num) for num in line.strip().split()]
    d = sqrt(x**2 + y**2)
    if d > r:
        print("miss")
    else:
        circle_area = pi * r**2
        h = r - d
        c = 2*sqrt(r**2 - d**2)
        angle = 2*(asin(c/(2*r)))
        segment_area = r**2/2 * (angle - sin(angle))
        print(circle_area - segment_area, segment_area)
