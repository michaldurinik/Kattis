#https://open.kattis.com/problems/downtime
from sys import stdin 
from math import ceil
from bisect import insort_right

tasks, jobs = stdin.readline().split()
server = [0]

for query in stdin:
    query = int(query)
    
    #always keep sorted list, compare with lowest time, del it and insert new task to correct place or
    #add new server to the end.
    #insort_right slightly faster than left? 
    
    if query >= server[0]:
        server.pop(0)
        insort_right(server, query + 1000)
    else:
        server.append(query + 1000)

#rounding up if decimal spaces, ie. 1more server needed 
     
print(ceil(len(server) / int(jobs)))