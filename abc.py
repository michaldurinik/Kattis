#https://open.kattis.com/problems/abc
from sys import stdin

nums = [int(x) for x in stdin.readline().strip().split()]
nums.sort()
order = stdin.readline().strip()

s = "ABC"
lst = []

for c in order:
    idx = s.find(c)
    lst.append(nums[idx])

lst = [str(s) for s in lst]
print(" ".join(lst))
