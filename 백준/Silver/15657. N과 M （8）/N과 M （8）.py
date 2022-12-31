import sys
def input(): return sys.stdin.readline().rstrip()

n, m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
b=[]

def f(start):
    if len(b) < m:
        for i in a:
            if len(b) != 0:
                if i >= b[-1]:
                    b.append(i)
                    f(i)
                    b.pop()
            else:
                b.append(i)
                f(i)
                b.pop()
    else:
        print(*b)

f(a[0])