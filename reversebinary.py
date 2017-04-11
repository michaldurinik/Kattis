#https://open.kattis.com/problems/reversebinary
from sys import stdin
n = int(stdin.readline().strip())

# bin(n) --> b0xxxx --> str --> reverse from 2nd index
reversed = str(bin(n))[:1:-1]
print(int(reversed, 2))