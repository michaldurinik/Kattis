#https://open.kattis.com/problems/tri
from sys import stdin

def test(x, y, z):
    if x + y == z:
        return "+="
        
    if x - y == z:
        return "-="
        
    if x * y == z:
        return "*="
    
    if x / y == z:
        return "/="
        
    if x == y + z:
        return "=+"

    if x == y - z:
        return "=-"

    if x == y * z:
        return "=*"
        
    if x == y / z:
        return "=/"
        
nums = stdin.readline().strip().split()
x, y, z = [int(x) for x in nums]
sigs = test(x, y, z)
print(str(x) + sigs[0] + str(y) + sigs[1] + str(z))