#https://open.kattis.com/problems/twostones
from sys import stdin
if int(stdin.readline().strip()) %2 == 0:
    print("Bob")
else:
    print("Alice")