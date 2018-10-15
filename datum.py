#https://open.kattis.com/problems/datum
import calendar
from sys import stdin

day, month = stdin.readline().strip().split()
print(calendar.day_name[calendar.weekday(2009, int(month), int(day))])
