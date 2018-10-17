#https://open.kattis.com/problems/akcija
from sys import stdin

_ = stdin.readline()
price_lst = []

for price in stdin:
    price_lst.append(int(price))

price_lst.sort()
price_lst.reverse()
discount = price_lst[2:][::3]
print(sum(price_lst) - sum(discount))
