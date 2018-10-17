#https://open.kattis.com/problems/aboveaverage
from sys import stdin

_ = stdin.readline()
for data in stdin:
    data = [int(x) for x in data.strip().split()]
    students, *score = data

    above_avg = 0
    avg = sum(score) / students
    for num in score:
        if num > avg:
            above_avg += 1
    print("{:2.3%}".format(above_avg / students))
