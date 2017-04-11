#https://open.kattis.com/problems/apaxiaaans
from sys import stdin

name = stdin.readline().strip()
letters = [name[0]]

i = 0
for idx, c in enumerate(name):
    if c != name[i]:
        letters.append(c)
        i = idx

print("".join(letters))