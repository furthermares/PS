import sys
def input(): return sys.stdin.readline().rstrip()

n, m = map(int,input().split())
a = []

def f(start):
    if len(a) < m:
        for i in range(start,n+1):
            a.append(i)
            f(i)
            a.pop()
    else:
        print(*a)

f(1)