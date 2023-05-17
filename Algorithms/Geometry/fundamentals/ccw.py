class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def ccw(p1, p2, p3):
    val = (p1.x*p2.y + p2.x*p3.y + p3.x*p1.y) - (p2.x*p1.y + p3.x*p2.y + p1.x*p3.y)
    
    if val > 0:
      # Clockwise orientation
      return 1
    elif val < 0:
      # Counterclockwise orientation
      return -1
    else:
      # Collinear orientation
      return 0

P = []
for _ in range(3):
    P.append(Point(*map(int,input().split())))

o = ccw(P[0], P[1], P[2])

if o == 1:
    print("Clockwise")
elif o == -1:
    print("CounterClockwise)
else:
    print("Colinear")
