import sys
a = [int(num) for num in sys.stdin.readline().strip().split()]
num = a[0]
capacity = a[-1]
a = a[1:-2]

print(num,capacity,a)