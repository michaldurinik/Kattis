#https://open.kattis.com/problems/modulo
from sys import stdin

num_lst = 42*[0] 
for num in stdin:
    num_lst[int(num)%42] += 1

print(len([x for x in num_lst if x != 0]))    