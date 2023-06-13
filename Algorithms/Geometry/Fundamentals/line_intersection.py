"""
https://icpc.me/17387
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
       return "({},{})".format(self.x, self.y)

class Line:
    def __init__(self, xs, ys, xe, ye):
        self.s = Point(xs, ys)
        self.e = Point(xe, ye)
    
    def __repr__(self):
        return "(({},{}),({},{}))".format(self.s.x, self.s.y, self.e.x, self.e.y)

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

# Check if lines 'l1' and 'l2' intersect
def lines_intersect(l1, l2):
    p1, q1 = l1.s, l1.e
    p2, q2 = l2.s, l2.e

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
L1, L2 = Line(x1,y1,x2,y2), Line(x3,y3,x4,y4)

print(lines_intersect(L1, L2))
