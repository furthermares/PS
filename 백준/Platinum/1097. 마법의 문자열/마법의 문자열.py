input = __import__('sys').stdin.readline
inp = lambda: int(input())
ins = lambda: input().rstrip()

from itertools import permutations

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

S = []
N = inp()
for _ in range(N):
    S.append(ins())
K = inp()

ans = 0

for perm in permutations(S[1:]):
    Si = S[0] + ''.join(perm)
    res = KMP((Si*2)[:-1], Si)
    if len(res) == K: ans += 1
print(ans * N)