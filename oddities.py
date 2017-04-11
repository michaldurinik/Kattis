#https://open.kattis.com/problems/oddities
from sys import stdin

_ = stdin.readline()
for line in stdin:
    num = int(line.strip())
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")