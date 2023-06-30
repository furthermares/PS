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

while True:
    S = ins()
    if S == ".": break
    n = len(S)
    
    lps = fail(S)

    if n % (n - lps[-1]):
        print(1)
    else:
        print(n // (n - lps[-1]))