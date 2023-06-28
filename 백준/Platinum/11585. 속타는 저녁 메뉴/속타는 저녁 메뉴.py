input = __import__('sys').stdin.readline
inp = lambda: int(input())
ins = lambda: input().rstrip()

from math import gcd

def fail(p):
    n = len(p)
    lps = [0] * n
    j = 0
    for i in range(1, n):
        while j and p[i] != p[j]:
            j = lps[j - 1]
        if p[i] == p[j]:
            j += 1
            lps[i] = j
    return lps

def KMP(t, p):
    lt, lp = len(t), len(p)
    res = []

    lps = fail(p)

    i = j = 0
    while i < lt:
        if t[i] == p[j]:
            i += 1
            j += 1
        else:
            if j:
                j = lps[j-1]
            else:
                i += 1
        
        if j == lp:
            res.append(i-j+1)
            j = lps[j-1]

    return res
    
N = inp()
A = [i for i in ins().split()]
B = [i for i in ins().split()]

res = len(KMP(A*2, B))

if A == B:
    res -= 1

d = gcd(res, N)
print(f"{res//d}/{N//d}")