#https://open.kattis.com/problems/conundrum
from sys import stdin

text = stdin.readline().strip()
pet = "Per" * (len(text) // 3)

unchanged = [x for x, y in zip(text, pet) if x == y.upper()]
print(len(text) - len(unchanged))
