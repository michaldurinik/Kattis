#https://open.kattis.com/problems/aaah
from sys import stdin

john = stdin.readline()
doctor = stdin.readline()

if len(john) < len(doctor):
    print("no")

else:
    print("go")
