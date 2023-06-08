import sys
input = sys.stdin.readline
inp = lambda: int(input())
inm = lambda: map(int,input().split())

from math import sqrt, ceil

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
        
def dist(p, q):
    return sqrt((p.x - q.x) ** 2 + (p.y - q.y) ** 2)
    
def distVE(o, a, b) :
    return abs((b - a).cross(o - a)) / dist(a,b)
    
def ccw(o, a, b):
    return (a - o).cross(b - o)

def convex_hull(points):
    points = sorted(set(points))
    
    if len(points) <= 1:
        return points
        
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in points[::-1]:
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

cnt = 0
while True:
    N = inp()
    if N == 0: break
    cnt += 1
    
    P = [Point(*inm()) for _ in range(N)]

    hull = convex_hull(P)
    n = len(hull)
    
    ans = sys.maxsize
    for i in range(n):
        localmx = 0.0
        e1 = hull[i-1]
        e2 = hull[i]
        for j in range(n):
            localmx = max(localmx, distVE(hull[j],e1,e2))
        ans = min(ans,localmx)

    print("Case {}: {:.2f}".format(cnt, ceil(ans*100)/100))
