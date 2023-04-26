import sys
def input(): return sys.stdin.readline().rstrip()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def orientation(p1, p2, p3):
    return (p1.x*p2.y + p2.x*p3.y + p3.x*p1.y) - (p2.x*p1.y + p3.x*p2.y + p1.x*p3.y)

P = []
for _ in range(3):
    P.append(Point(*map(int,input().split())))

res = orientation(P[0], P[1], P[2])

if res > 0:
    print(1)
elif res < 0:
    print(-1)
else:
    print(0)