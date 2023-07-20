import sys
def input(): return sys.stdin.readline().rstrip()

import math

A1, P1 = map(int,input().split())
R1, P2 = map(int,input().split())

R1 = R1*R1*math.pi

if A1/P1 > R1/P2:
    print("Slice of pizza")
else:
    print("Whole pizza")