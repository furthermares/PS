input = __import__('sys').stdin.readline
ins = lambda: input().rstrip()

from collections import deque

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

    lps = fail(p)
    
    i = j = 0
    j_his = deque([0])
    while i < lt:
        if t[i] == p[j]:
            i += 1
            j += 1
            j_his.append(j)
        else:
            if j:
                j = lps[j-1]
            else:
                i += 1
                j_his.append(j)
        
        if j == lp:
            t = t[:i - lp] + t[i:]
            for _ in range(lp): j_his.pop()
            j = j_his[-1]
            lt -= lp
            i -= lp

    print(t)

S = ins()
T = ins()

KMP(S, T)