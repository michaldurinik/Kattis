#https://open.kattis.com/problems/tarifa
from sys import stdin

minutes = int(stdin.readline().strip())
months = int(stdin.readline().strip())
total = minutes * (months + 1)

for num in stdin:
    num = int(num.strip())
    total -= num
    
print(total)