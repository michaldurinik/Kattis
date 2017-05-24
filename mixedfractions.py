#https://open.kattis.com/problems/mixedfractions
from sys import stdin

for line in stdin:
    line = line.strip().split()
    
    if line != ["0", "0"]:
        num = int(line[0])
        div = int(line[1])
        print(num // div, num % div, "/", div)