#https://open.kattis.com/problems/pot

from sys import stdin

total = 0
numbers = stdin.readline()

for num in stdin:
    num = num.strip()
    total += int(num[:-1]) ** int(num[-1])
    
print(total)