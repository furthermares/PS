input = __import__('sys').stdin.readline
inp = lambda: int(input())
ins = lambda: input().rstrip()
insl = lambda: list(input()[:-1])

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

for _ in range(inp()):
    A, W, S = ins(), ins(), insl()
    shift = {A[i]:A[i-1] for i in range(len(A))}
    
    ans = []
    for i in range(len(A)):
        if len(KMP(S, W)) == 1:
            ans.append(i)
        
        for j in range(len(S)):
            S[j] = shift[S[j]]

    n = len(ans)
    if n == 0:
        print("no solution")
    elif n == 1:
        print("unique:", ans[0])
    else:
        print("ambiguous:", *ans)