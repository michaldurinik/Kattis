#https://open.kattis.com/problems/kemija08
from sys import stdin
text = list(stdin.readline().strip())
translated = []

i = 0
while i < len(text):
    if text[i] not in "aeiou":
        translated.append(text[i])
    else:
        translated.append(text[i])
        i += 2
    i += 1
    
print("".join(translated))