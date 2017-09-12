#https://open.kattis.com/problems/oddmanout
from sys import stdin
from collections import Counter

cases = int(stdin.readline().strip())
for i in range(1, cases + 1):
    _ = stdin.readline()
    nums = stdin.readline().strip().split()

    # unique element(count=1) is in first tuple
    lst = sorted(Counter(nums).items(), key=lambda x:x[1])
    print("Case #" + str(i) + ": " + lst[0][0])
