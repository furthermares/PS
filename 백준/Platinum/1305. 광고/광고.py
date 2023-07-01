input = __import__('sys').stdin.readline
inp = lambda: int(input())
ins = lambda: input().rstrip()

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

L = inp()
T = ins()

lps = fail(T)

print(L - lps[-1])