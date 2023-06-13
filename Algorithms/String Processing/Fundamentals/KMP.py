"""
https://icpc.me/1786
"""

def KMP(t, p): #text, pattern
    lt, lp = len(t), len(p)
    res = []
    # create lps[] that will hold the longest prefix suffix values for pattern
    lps = [0] * lp

    # Preprocess the pattern (calculate lps[] array)
    computeLPS(p, lps)

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

def computeLPS(p, lps):
    length = 0 # length of the previous longest prefix suffix

    i = 1
    # the loop calculates lps[i] for i = 1 to len(p)-1
    while i < len(p):
        if p[length] == p[i]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # This is tricky. Consider the example. AAACAAAA and i = 7. The idea is similar to search step.
            if length == 0:
                lps[i] = 0
                i += 1
                
                # Also, note that we do not increment i here
            else:
                length = lps[length-1]

T = input() # Text
P = input() # Pattern
res = KMP(T, P)

print(len(res))
print(*res)
