#https://open.kattis.com/problems/zamka
from sys import stdin

low = int(stdin.readline().strip())
high = int(stdin.readline().strip())
digit_sum = int(stdin.readline().strip())

for n in range(low, high+1):
    lst = list(str(n))
    if sum([int(x) for x in lst]) == digit_sum:
        print(n)
        break

for n in range(high, low-1, -1):
    lst = list(str(n))
    if sum([int(x) for x in lst]) == digit_sum:
        print(n)
        break