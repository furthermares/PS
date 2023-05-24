import sys
def input(): return sys.stdin.readline().rstrip()
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(p1, p2, p3):
    val = (p1.x*p2.y + p2.x*p3.y + p3.x*p1.y) - (p2.x*p1.y + p3.x*p2.y + p1.x*p3.y)
    if val > 0:
      return 1
    elif val < 0:
      return -1
    else:
      return 0

x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())
L1s, L1e, L2s, L2e = Point(x1,y1), Point(x2,y2), Point(x3,y3), Point(x4,y4)

if ccw(L1s,L1e,L2s)*ccw(L1s,L1e,L2e) < 0 and ccw(L2s,L2e,L1s)*ccw(L2s,L2e,L1e) < 0:
    print(1)
else:
    print(0)