input = __import__('sys').stdin.readline
inp = lambda: int(input())
inm = lambda: map(int,input().split())
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
    res = False

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
            res = True
            j = lps[j-1]

    return res
    
N, K = inm()
Mi = []
M = []
min_Mi = 1001
min_Mi_idx = 0
for i in range(N):
    t = inp()
    Mi.append(t)
    if t < min_Mi:
        min_Mi = min(min_Mi, t)
        min_Mi_idx = i
    M.append(inl())

for i in range(min_Mi-K+1):
    p = M[min_Mi_idx][i:i+K]
    
    for j in range(N):
        if p == min_Mi_idx:
            continue
            
        if not KMP(M[j] + [-1] + M[j][::-1], p):
            break
    else:
        break
else:
    print("NO")
    exit(0)
print("YES")