#https://open.kattis.com/problems/spavanac
from sys import stdin

def to_min(h, m):
    return h*60 + m - 45
    
def to_hours(m):
    print(m//60%24, m%60)
    
h, m = [int(x) for x in stdin.readline().strip().split()]
to_hours(to_min(h, m))