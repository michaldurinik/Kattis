#https://open.kattis.com/problems/skener
from sys import stdin
data = stdin.readline().strip().split()
rows, columns, multR, multC = [int(x) for x in data]

matrix = []
for line in stdin:
    line = list(line.strip())
    line = [x for x in line for y in range(multC)]
    for i in range(multR):
        matrix.append(line)

for row in matrix:
    print("".join(row))