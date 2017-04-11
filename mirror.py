#https://open.kattis.com/problems/mirror
from sys import stdin
tests = int(stdin.readline().strip())
test = 1

for i in range(tests):
    rows, columns = stdin.readline().strip().split()
    rows = int(rows)
    columns = int(columns)
    a = []

    print("Test", test)
    for i in range(rows):
        a.append(list(stdin.readline().strip()))
        
    test += 1
    a = reversed(a)   
    for lst in a:
        print("".join(reversed(lst)))
