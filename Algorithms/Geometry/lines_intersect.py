"""
https://www.acmicpc.net/submit/12781
"""

import sys
def input(): return sys.stdin.readline().rstrip()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Given three collinear points p, q, r, check if point q lies on line 'pr'
def on_segment(p, q, r):
    if q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y):
        return True
    return False

# ccw
def ccw(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:
        return 0

# Check if segment 'p1q1' and 'p2q2' intersect
def lines_intersect(p1,q1,p2,q2):
    o1 = ccw(p1, q1, p2)
    o2 = ccw(p1, q1, q2)
    o3 = ccw(p2, q2, p1)
    o4 = ccw(p2, q2, q1)

    # General case
    if ((o1 != o2) and (o3 != o4)): return True
    
    # Special cases
    # First line checks p1, q1, p2 are collinear + p2 lies on line p1q1. Check for all 4.
    if ((o1 == 0) and on_segment(p1, p2, q1)): return True
    if ((o2 == 0) and on_segment(p1, q2, q1)): return True
    if ((o3 == 0) and on_segment(p2, p1, q2)): return True
    if ((o4 == 0) and on_segment(p2, q1, q2)): return True

    return False

x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())
L1s, L1e, L2s, L2e = Point(x1,y1), Point(x2,y2), Point(x3,y3), Point(x4,y4)

print(1 if lines_intersect(L1s, L1e, L2s, L2e) else 0)
