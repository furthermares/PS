import sys
input = sys.stdin.readline
inp = lambda: int(input())
inm = lambda: map(int,input().split())

import math

class Point:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        
    def __lt__(self, other):
        return self.x < other.x if self.x != other.x else self.y < other.y

    def incl(self, other):
        return math.inf if self.x == other.x else (self.y - other.y)/(self.x - other.x), self.x, self.y

for _ in range(inp()):
    N, *t = inm()
    P = []
    for i in range(N):
        P.append(Point(t[i*2], t[i*2+1], i))
    
    p = min(P)
    idx = P.index(p)
    P[0], P[idx] = P[idx], P[0]
    P = [P[0]] + sorted(P[1:], key = lambda x: x.incl(p))

    i = -2
    t = P[0].incl(P[-1])
    while True:
        if P[0].incl(P[i]) != t:
            break
        i -= 1
    P = P[:i+1] + P[:i:-1]
    
    for i in P:
        print(i.idx, end=' ')
    print()