#https://open.kattis.com/problems/kitten
from sys import stdin
kitten = stdin.readline().strip()
tree = {}
path = [kitten]
found = False

for line in stdin:
    line = line.strip().split()
    tree[line[0]] = set(line[1:])

for i in range(len(tree)):     #until max of all paths, instead of while True
    for k, v in tree.items():
        if kitten in v:
            kitten = k
            path.append(k)
            found = True
            break
            
    if not found:
        break

print(" ".join(path))