#https://open.kattis.com/problems/almostperfect
from sys import stdin

for num in stdin:
    num = int(num.strip())
    
    i = 2
    total = 1
    while i + total < num + 3:
        if num % i == 0:
            total += i
        
        i += 1
            
    if total == num:
        print(num, "perfect")
    elif total + 1 == num or total + 2 == num or total - 1 == num or total - 2 == num:
        print(num, "almost perfect")
    else:
        print(num, "not perfect")
    