input = __import__('sys').stdin.readline
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

S = ins()

lps = fail(S)

for i in range(1, len(S)+1):
    if lps[i-1] and not i % (i - lps[i-1]):
        print(i, i // (i - lps[i-1]))