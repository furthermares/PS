from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __lt__(self, other):
        return self.x < other.x if self.x != other.x else self.y < other.y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def __repr__(self):
       return "({},{})".format(self.x, self.y)

def dist(p, q):
    return sqrt((p.x - q.x) ** 2 + (p.y - q.y) ** 2)

def distVE(E, A, B) :
    AB = B-A
    BE = E-B
    AE = E-A

    if AB.dot(BE) > 0:
        return dist(B,E)
    if AB.dot(AE) < 0:
        return dist(A,E)
    return abs(AB.cross(AE)) / dist(A,B)

def area(points):
    ans = 0
    for i in range(len(points)):
        ans += points[i].cross(points[i-1])
    return abs(ans/2)

def ccw(o, a, b):
    return (a - o).cross(b - o)
