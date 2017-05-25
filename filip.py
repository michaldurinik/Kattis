#https://open.kattis.com/problems/filip
from sys import stdin
nums = [x[::-1] for x in stdin.readline().strip().split()]
print(sorted(nums)[1])
