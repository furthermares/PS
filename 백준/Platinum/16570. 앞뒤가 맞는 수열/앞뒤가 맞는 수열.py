input = __import__('sys').stdin.readline
inp = lambda: int(input())
inl = lambda: list(map(int,input().split()))

from collections import Counter

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

N = inp()
A = inl()

lps = fail(A[::-1])

mx = max(lps)
print(mx, Counter(lps)[mx]) if mx else print(-1)