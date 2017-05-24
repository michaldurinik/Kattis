#https://open.kattis.com/problems/autori
from sys import stdin
name = stdin.readline().strip().split("-")
print("".join([x[0] for x in name]))
