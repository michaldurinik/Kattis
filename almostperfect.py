#https://open.kattis.com/problems/almostperfect
from sys import stdin
from math import sqrt

def factors(n):
    a = [[i, n//i] for i in range(2, int(sqrt(num)) + 1) if n % i == 0]
    return set([x for pair in a for x in pair])

for num in stdin:
    num = int(num.strip())

    #1 and num itself was excluded in factors
    total = sum(factors(num)) + 1

    if total == num:
        print(num, "perfect")
    elif abs(total - num) <= 2:
        print(num, "almost perfect")
    else:
        print(num, "not perfect") 
