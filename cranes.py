#https://open.kattis.com/problems/cranes
from sys import stdin
from itertools import combinations

class Crane_obj(object):

    def __init__(self, id, coords):
        self.coords = coords
        self.id = id
        self.overlap = []
    
    def get_coords(self):
        return self.coords

    def get_overlap(self):
        return self.overlap

    def add_overlap(self, num):
        self.overlap.append(num)
    
    def get_id(self):
        return self.id

    def __str__(self):
        return "{}: {} {}".format(self.id, self.coords, self.overlap)
    

def overlaps(lst1, lst2):
    x1, y1, r1 = lst1
    x2, y2, r2 = lst2
    return (r1 + r2)**2 > (x1 - x2)**2 + (y1 - y2)**2

tests = int(stdin.readline().strip())
for test in range(tests):
    cranes = int(stdin.readline().strip())
    id = 1
    lst = []

    for i in range(cranes):
        coords = [int(num) for num in stdin.readline().strip().split()]
        lst.append(Crane_obj(id, coords))
        id += 1

    for pair in combinations(lst, 2):
        c1 = pair[0]
        c2 = pair[1]
        if overlaps(c1.get_coords(), c2.get_coords()):
            c1.add_overlap(c2.get_id())
            c2.add_overlap(c1.get_id())

    for obj in lst:
        print(obj)
