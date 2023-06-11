import sys
input = sys.stdin.readline
inm = lambda: map(int,input().split())

import math

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

def dist(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def ccw(o, a, b):
    val = (a - o).cross(b - o)
    if val > 0:
      return 1
    elif val < 0:
      return -1
    else:
      return 0
     
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

N, R = inm()
P = [Point(*inm()) for _ in range(N)]

hull = convex_hull(P)

ans = 2 * math.pi * R
for i in range(len(hull)):
    ans += dist(hull[i-1], hull[i])

print(ans)