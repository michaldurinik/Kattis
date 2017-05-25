from sys import stdin
tests = int(stdin.readline())

for test in range(tests):
    lines = int(stdin.readline())
    phonebook = {
        1: set(),
        2: set(),
        3: set(),
        4: set(),
        5: set(),
        6: set(),
        7: set(),
        8: set(),
        9: set(),
        10: set(),}
        
    for num in range(lines):
        num = stdin.readline().strip()

        found = False
        for i in range(1, len(num)):
            if num[:i] in phonebook[i]:
                print("NO")
                found = True
                break

        if not found:
            phonebook[len(num)].add(num)
            
    if not found:
        print("YES")
