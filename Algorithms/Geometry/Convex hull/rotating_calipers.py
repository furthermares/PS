"""
https//icpc.me/9240
Time Complexity: O(NlogN) 
Auxiliary Space: O(N)
"""

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

def dist(p, q):
    return math.sqrt((p.x - q.x) ** 2 + (p.y - q.y) ** 2)

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

def rotating_calipers(points):
    hull = convex_hull(P)
    n = len(hull)
 
    # Base Cases
    if n == 1:
        return 0
    if n == 2:
        return dist(hull[0],hull[1])

    k = 1
    # Find the farthest vertex from hull[0] and hull[n-1]
    while ccw(hull[n - 1], hull[0], hull[(k + 1) % n]) > ccw(hull[n - 1], hull[0], hull[k]):
        k += 1
 
    res = 0
    # Check points from 0 to k
    for i in range(k + 1):
        j = (i + 1) % n
        while ccw(hull[i], hull[(i + 1) % n], hull[(j + 1) % n]) > ccw(hull[i], hull[(i + 1) % n], hull[j]):
            # Update res
            res = max(res, dist(hull[i], hull[(j + 1) % n]))
            j = (j + 1) % n
 
    # Return the result distance
    return res
    
C = inp()
P = [Point(*map(int,input().split())) for _ in range(C)]

print(rotating_calipers(P))
