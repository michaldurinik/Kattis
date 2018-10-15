#https://open.kattis.com/problems/hissingmicrophone
from sys import stdin

word = stdin.readline()
if "ss" in word:
    print("hiss")
else:
    print("no hiss")
