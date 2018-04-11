#https://open.kattis.com/problems/listgame
from sys import stdin
from math import sqrt

def lowest_divisor(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return i
    return num

#last divisor is never added so counter starts at 1
counter = 1
num = int(stdin.readline().strip())

while lowest_divisor(num) != num:
    counter += 1
    num = num // lowest_divisor(num)

print(counter)
