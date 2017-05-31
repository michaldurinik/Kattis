#https://open.kattis.com/problems/classy
from sys import stdin
tests = int(stdin.readline().strip())

for test in range(tests):
    lines = int(stdin.readline().strip())
    
    lst = []
    for line in range(lines):

        #["name:", "upper-lower...."]
        *line, _ = stdin.readline().strip().split()             
        name, details = line

        # ["u",p,l,m,...]
        details = [x[0] for x in details.split("-")]            
        extra_m = ["m"] * (10 - len(details))
        lst.append([name[:-1], details[::-1] + extra_m])
    
    # sorting alphabetically
    lst.sort()

    #sorting by destription of class
    for pair in sorted(lst, key=lambda x: x[1], reverse=True):
        print(pair[0])

    print("=" * 30)    
