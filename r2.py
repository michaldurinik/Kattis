#https://open.kattis.com/problems/r2
from sys import stdin
nums = stdin.readline().strip().split()
r1 = int(nums[0])
mean = int(nums[1])

r2 = r1 + (mean - r1)*2
print (r2)


