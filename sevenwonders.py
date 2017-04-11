#https://open.kattis.com/problems/sevenwonders
from sys import stdin
cards = stdin.readline().strip()

tablet = cards.count("T")
compass = cards.count("C")
gear = cards.count("G")

score = tablet**2 + compass**2 + gear**2
bonus = min([tablet, compass, gear]) * 7

if tablet and compass and gear:
    score += bonus
    
print(score)