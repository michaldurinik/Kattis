#https://open.kattis.com/problems/soylent
from sys import stdin
from math import ceil
CALORIES = 400

_ = stdin.readline()

for num in stdin:
    num = int(num.strip())
    print(ceil(num / CALORIES))