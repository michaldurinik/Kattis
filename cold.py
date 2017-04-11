#https://open.kattis.com/problems/cold
from sys import stdin

_ = stdin.readline()
print(len([neg for neg in stdin.readline().strip().split() if int(neg) < 0]))



