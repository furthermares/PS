import sys
input = sys.stdin.readline
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
    ret = []
    
    lps = fail(p)
    
    j = 0
    for i in range(lt):
        while j and t[i] != p[j]:
            j = lps[j-1]
            
        if t[i] == p[j]:
            j += 1
            if j == lp:
                ret.append(i-j+1)
                j = lps[j-1]
                
    return ret

N = inp()
T = inl()

lps = fail(T[::-1])

k = p = 0
mn = sys.maxsize
for i in range(N):
    ki = len(lps) - (i+1)
    pi = (i+1) - lps[i]
    if ki + pi < mn:
        mn = ki + pi
        k, p = ki, pi
print(k,p)