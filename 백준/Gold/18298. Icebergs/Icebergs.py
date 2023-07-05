input = __import__('sys').stdin.readline
inp = lambda: int(input())
inm = lambda: map(int,input().split())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def cross(self, other):
        return self.x * other.y - self.y * other.x

def area(points):
    ret = 0
    for i in range(len(points)):
        ret += points[i].cross(points[i-1])
    return abs(ret/2)
    
ans = 0
for _ in range(int(input())):
    N = inp()
    S = [Point(*inm()) for _ in range(N)]
    
    ans += area(S)

print(int(ans))