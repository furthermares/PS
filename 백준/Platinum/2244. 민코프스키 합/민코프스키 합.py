import sys
input = sys.stdin.readline
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

N, M = inm()
A = [Point(*inm()) for _ in range(N)]
B = [Point(*inm()) for _ in range(M)]
P = []
for i in range(N):
    for j in range(M):
        P.append(Point(A[i].x+B[j].x, A[i].y+B[j].y))

res = convex_hull(P)

print(len(res))
for p in res:
    print(p.x, p.y)