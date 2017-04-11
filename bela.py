#https://open.kattis.com/problems/bela
from sys import stdin

dom = {"A":11,
       "K":4,
       "Q":3,
       "J":20,
       "T":10,
       "9":14}
       
not_dom = {"A":11,
           "K":4,
           "Q":3,
           "J":2,
           "T":10}

_, suit = stdin.readline().strip().split()

total = 0

for card in stdin:
    card = card.strip()
    if card[1] == suit:
        if card[0] in dom:
            total += dom[card[0]]
    else:
        if card[0] in not_dom:
            total += not_dom[card[0]]
        
print(total)