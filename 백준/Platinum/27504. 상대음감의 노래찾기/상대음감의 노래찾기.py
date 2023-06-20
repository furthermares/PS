input = __import__('sys').stdin.readline
inp = lambda: int(input())
inl = lambda: list(map(int,input().split()))

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
K = [[] for _ in range(N)]
for i in range(N):
    prev, *Ki = inl()
    for cur in Ki:
        t = cur - prev
        K[i].append(t)
        prev = cur

input()
B = []
prev, *Bi = inl()
for cur in Bi:
    t = cur - prev
    B.append(t)
    prev = cur

ans = []
for i in range(N):
    if KMP(K[i], B):
        ans.append(i+1)
print(*ans) if ans else print(-1)