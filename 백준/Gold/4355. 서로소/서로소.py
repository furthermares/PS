import sys
def input(): return sys.stdin.readline().rstrip()

def phi(n):
    res = n
    p = 2
    while (p*p <= n):
        if (n%p == 0):
            while (n%p == 0):
                n = int(n/p)
            res -= int(res/p) 
        p += 1
    if (n>1):
        res -= int(res/n)
    return res

while (True):
    N = int(input())
    if (N == 0): break
    elif (N == 1): print(0)
    else: print(phi(N))