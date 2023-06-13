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
