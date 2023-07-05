from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __lt__(self, other):
        return self.x < other.x if self.x != other.x else self.y < other.y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __hash__(self):
        return hash((self.x, self.y))
        
    def __repr__(self):
       return f"({self.x}, {self.y})"

def dist(p, q):
    return sqrt((p.x - q.x) ** 2 + (p.y - q.y) ** 2)

# Distance between a point and a line segment. For line, comment lines with dot product.
def distVE(E, A, B):
    AB = B-A
    BE = E-B
    AE = E-A

    if AB.dot(BE) > 0:
        return dist(B,E)
    if AB.dot(AE) < 0:
        return dist(A,E)
    return abs(AB.cross(AE)) / dist(A,B)

def area(points):
    ret = 0
    for i in range(len(points)):
        ret += points[i].cross(points[i-1])
    return abs(ret/2)

def ccw(o, a, b):
    return (a - o).cross(b - o)
