#https://open.kattis.com/problems/easiest
from sys import stdin

def to_sum(n):
   s = 0
   while n:
       s, n = s + n % 10, n // 10
   return s
    
for line in stdin:
    line = int(line.strip())
    if line == 0:
        break
        
    i = 11
    while True:
        if to_sum(line) == to_sum(line * i):
            print(i)
            break
        i += 1