#https://open.kattis.com/problems/symmetricorder
from sys import stdin

count = 1
for num in stdin:
    num = int(num.strip())
    if num == 0:
        break
    print("SET", count) 
    
    pairs_dict = {}
    for i in range(1, num+1):
        line = stdin.readline().strip()
        pairs_dict[i] = line
    
    for k, v in sorted(pairs_dict.items()):
        if not k % 2 == 0:
            print(v)
    
    for k, v in sorted(pairs_dict.items(), reverse = True):
        if k % 2 == 0:
            print(v)
    
    count += 1