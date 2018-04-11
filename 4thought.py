#https://open.kattis.com/problems/4thought
from sys import stdin

test_cases = stdin.readline()

for num in stdin:
    num = int(num.strip())
    reminder = num % 4
    if reminder == 2:
        print("no solution")

    else:
        print("123")
