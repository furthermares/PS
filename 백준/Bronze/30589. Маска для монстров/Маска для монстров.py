input=__import__('sys').stdin.readline
inp=lambda:int(input())
inm=lambda:map(int,input().split())

from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x if self.x != other.x else self.y < other.y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

def dist(p, q):
    return sqrt((p.x - q.x) ** 2 + (p.y - q.y) ** 2)

N=inp()
v=[Point(*inm()) for _ in[0]*N]

d=[dist(v[i],v[i-1]) for i in range(N)]
print("%.6f"%(sum(d)-max(d)))