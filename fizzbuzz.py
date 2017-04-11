#https://open.kattis.com/problems/fizzbuzz
from sys import stdin
fizz, buzz, fb = [int(x) for x in stdin.readline().strip().split()]

for num in range(1,fb+1):
    if num % fizz == 0 and num % buzz == 0:
        print("FizzBuzz")
        continue
    if num % fizz == 0:
        print("Fizz")
        continue
    if num % buzz == 0:
        print("Buzz")
        continue    
    print(num)