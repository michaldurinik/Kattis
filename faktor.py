#https://open.kattis.com/problems/faktor
from sys import stdin

art, cit = [int(x) for x in stdin.readline().strip().split()]
print(art * cit - (art - 1))
