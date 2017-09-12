#https://open.kattis.com/problems/kornislav
from sys import stdin

nums = sorted([int(x) for x in stdin.readline().strip().split()])
#smallest * second biggest, other 2 are ignored
print(nums[0] * nums[2])
