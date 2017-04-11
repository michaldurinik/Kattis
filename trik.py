#https://open.kattis.com/problems/trik
from sys import stdin

a = [1,0,0]

def swap(i,j):
   a[j], a[i] = a[i], a[j] 

for c in stdin.readline().strip():
    if c == "A":
        swap(0,1)
    if c == "B":
        swap(1,2)
    if c == "C":
        swap(0,2)
        
print(a.index(1)+1)