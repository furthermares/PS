import sys
input = sys.stdin.readline
inm = lambda: map(int,input().split())
from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def dot(x1, y1, x2, y2):
    return x1*x2 + y1*y2

def cross(x1, y1, x2, y2):
    return x1*y2 - x2*y1

def perpendicular_dist(x1, y1, x2, y2, px, py):
    dot1 = dot(x2-x1, y2-y1, px-x1, py-y1)
    dot2 = dot(x1-x2, y1-y2, px-x2, py-y2)

    if dot1*dot2 >= 0:
        return abs(cross(x2-x1, y2-y1, px-x1, py-y1)) / distance(x1, y1, x2, y2)
    return -1
    
N, M = inm()

lineN = []
lineM = []

for _ in range(N):
    lineN.append(tuple(map(float,input().split())))
for _ in range(M):
    lineM.append(tuple(map(float,input().split())))

res = -1
for i in range(N):
    for j in range(M):
        nx1, ny1, nx2, ny2 = lineN[i]
        mx1, my1, mx2, my2 = lineM[j]
        
        dist = distance(nx1, ny1, mx1, my1)
        dist = min(dist, distance(nx1, ny1, mx2, my2))
        dist = min(dist, distance(nx2, ny2, mx1, my1))
        dist = min(dist, distance(nx2, ny2, mx2, my2))

        temp = perpendicular_dist(nx1, ny1, nx2, ny2, mx1, my1)
        if temp >= 0: dist = min(dist, temp)
        temp = perpendicular_dist(nx1, ny1, nx2, ny2, mx2, my2)
        if temp >= 0: dist = min(dist, temp)
        temp = perpendicular_dist(mx1, my1, mx2, my2, nx1, ny1)
        if temp >= 0: dist = min(dist, temp)
        temp = perpendicular_dist(mx1, my1, mx2, my2, nx2, ny2)
        if temp >= 0: dist = min(dist, temp)

        if res < 0:
            res = dist
        else:
            res = min(res, dist)

print(res)