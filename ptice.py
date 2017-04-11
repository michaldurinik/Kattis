#https://open.kattis.com/problems/ptice
from sys import stdin

tests = int(stdin.readline().strip())
seq = stdin.readline().strip()

Adrian = "ABC" * (len(seq)//3 + len(seq)%3)
Bruno = "BABC" * (len(seq)//4 + len(seq)%4)
Goran = "CCAABB" * (len(seq)//6 + len(seq)%6)

score = [[0, "Adrian"], [0, "Bruno"], [0, "Goran"]]

for idx, char in enumerate(seq):
    if char == Adrian[idx]:
        score[0][0] += 1
        
    if char == Bruno[idx]:
        score[1][0] += 1
        
    if char == Goran[idx]:
        score[2][0] += 1
        
score =  sorted(score, key = lambda x:x[0], reverse = True)
max = score[0][0]
print (max)

for pts, name in score:
    if pts != max:
        break
    print(name)