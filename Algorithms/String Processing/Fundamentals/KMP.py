"""
https://icpc.me/1786
"""

def fail(p):
    n = len(p)
    # create lps[] that will hold the longest prefix suffix values for pattern
    lps = [0] * n
    j = 0
    for i in range(1, n):
        while j and p[i] != p[j]:
            j = lps[j - 1]
        if p[i] == p[j]:
            j += 1
            lps[i] = j
    return lps

def KMP(t, p): #text, pattern
    lt, lp = len(t), len(p)
    res = []

    # Preprocess the pattern (calculate lps[] array)
    lps = fail(p)

    i = j = 0 # index for t[], p[]
    while i < lt:
        if t[i] == p[j]:
            i += 1
            j += 1

        # mismatch after j matches
        else:
            # Do not match lps[0..lps[j-1]] characters, they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
        
        if j == lp:
            res.append(i-j+1) #Found pattern at index i-j
            j = lps[j-1]

    return res

T = input() # Text
P = input() # Pattern
lps = KMP(T, P)

print(len(lps))
print(*lps)
