import sys
def input(): return sys.stdin.readline().rstrip()
from math import sqrt

for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    d = sqrt((x1-x2)**2 + (y1-y2)**2)

    if r1 == r2 and d == 0:
        print(-1)
    elif r1+r2 < d or abs(r1-r2) > d and r1 != r2:
        print(0)
    elif r1+r2 == d or abs(r1-r2) == d:
        print(1)
    elif r1+r2 > d > abs(r1-r2):
        print(2)