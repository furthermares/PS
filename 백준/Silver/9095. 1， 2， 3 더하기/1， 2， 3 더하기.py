import sys
def input(): return sys.stdin.readline().rstrip()

MAX = 10

d=[1]+[1]+[2]+[4]+[0]*(MAX-3)
for i in range(MAX-2):
    d[i+3] = d[i] + d[i+1] + d[i+2]

T = int(input())
for _ in range(T):
    N = int(input())
    print(d[N])