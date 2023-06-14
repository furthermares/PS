input = __import__('sys').stdin.readline
ins = lambda: input().rstrip()

def computeLPS(p, lps):
    length = 0

    i = 1
    while i < len(p):
        if p[length] == p[i]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length == 0:
                lps[i] = 0
                i += 1
            else:
                length = lps[length-1]

def KMP(t, p):
    lt, lp = len(t), len(p)
    res = []
    lps = [0] * lp

    computeLPS(p, lps)

    i = j = 0
    while i < lt:
        if t[i] == p[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        
        if j == lp:
            res.append(i-j+1)
            j = lps[j-1]

    return res

T = ins()
P = ins()
res = KMP(T, P)

print(len(res))
print(*res)