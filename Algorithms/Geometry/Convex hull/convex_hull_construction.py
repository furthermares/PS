# Monotone chain
"""
# https://icpc.me/1708
# Time Complexity: O(n log n)
"""

import sys
input = sys.stdin.readline
inp = lambda: int(input())
inm = lambda: map(int,input().split())

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

    def __repr__(self):
       return "({},{})".format(self.x, self.y)
        
def ccw(o, a, b):
    val = (a - o).cross(b - o)
    if val > 0:
      return 1
    elif val < 0:
      return -1
    else:
      return 0
     
def convex_hull(points):
    # Sort the points lexicographically
    points = sorted(set(points))
    
    # case for no points or a single point
    if len(points) <= 1:
        return points
        
    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in points[::-1]:
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list. 
    return lower[:-1] + upper[:-1]

N = inp()
Points = [Point(*inm()) for _ in range(N)]

print(len(convex_hull(Points)))
