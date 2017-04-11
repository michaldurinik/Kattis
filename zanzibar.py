#https://open.kattis.com/problems/zanzibar
from sys import stdin
_ = stdin.readline()

for records in stdin:
    records = [int(x) for x in records.strip().split()]
    imported = 0
    for i in range(len(records)-1):
        if records[i+1] > 2*records[i]:             #turtle can at maximum double population every year
            imported += records[i+1] - 2*records[i]
    
    print(imported)