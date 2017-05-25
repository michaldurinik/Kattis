#https://open.kattis.com/problems/phonelist
from sys import stdin
tests = int(stdin.readline())

def is_in(num):
    for i in range(1, len(num)):
        if num[:i] in phonebook_set:
            return True

    return False
             

for test in range(tests):
    lines = int(stdin.readline())
    phonebook = []
    phonebook_set = set()
    
    for num in range(lines):
        num = stdin.readline().strip()
        phonebook.append(num)
        phonebook_set.add(num)

    phonebook = sorted(phonebook, key=len, reverse=True)
    
    #check list from longest to smallest if they in set of all nums
    #checks every length of num from 1 to len(num)
    for idx, num in enumerate(phonebook):
        if is_in(num):
            print("NO")
            break

    if idx == len(phonebook) -1:
        print("YES")
