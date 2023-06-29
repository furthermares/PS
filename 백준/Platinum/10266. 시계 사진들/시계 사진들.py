input = __import__('sys').stdin.readline
inm = lambda: map(int,input().split())

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
    
MAX = 360000
input()
A = [False] * MAX
B = [False] * MAX

for i in inm():
    A[i] = True
for i in inm():
    B[i] = True

res = KMP(A*2, B)

if res:
    print("possible")
else:
    print("impossible")