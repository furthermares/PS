import sys
input = sys.stdin.readline
inp = lambda: int(input())
inm = lambda: map(int,input().split())

class Point:
    def __init__(self, x, y, idx=0):
        self.x = x
        self.y = y
        self.idx = idx
        
    def __lt__(self, other):
        return self.x < other.x if self.x != other.x else self.y < other.y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def cross(self, other):
        return self.x * other.y - self.y * other.x

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

def on_segment(p, q, r):
    if q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y):
        return True
    return False
    
N = inp()
P = [Point(*inm()) for _ in range(N)]

cnt = 1
while True:
    P_left = [p for p in P if p.idx == 0]

    if len(P_left) < 3:
        break

    res = convex_hull(P_left)

    area = 0
    for i in range(len(res)):
        area += res[i].cross(res[i-1])
        
    if area == 0:
        break
    else:
        for p in res:
            p.idx = cnt

    cnt += 1

for p in P:
    print(p.idx, end=' ')