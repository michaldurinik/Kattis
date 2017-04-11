import sys
no_samples = sys.stdin.readline()

i = 0
while i < int(no_samples):
    found = False
    number_count = int(sys.stdin.readline())
    seen = set()

    for line in range(number_count):
        line = sys.stdin.readline().strip()

        if not found:
            for idx in range(1, len(line)+1):
                if line[:idx] in seen:
                    found = True
                    print("NO")
                    break
                    
            seen.add(line)
            
        else:
            break

    if not found:
        print("YES")
    
    i += 1  