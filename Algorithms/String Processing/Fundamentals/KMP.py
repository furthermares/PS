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
    ret = []

    # Preprocess the pattern (calculate lps[] array)
    lps = fail(p)
    
    j = 0 # index for p
    for i in range(lt): # index for t
        while j and t[i] != p[j]: # mismatch after j matches
            # Do not match lps[0..lps[j-1]] characters, they will match anyway
            j = lps[j-1]
            
        if t[i] == p[j]:
            j += 1
            if j == lp:
                ret.append(i-j+1) # Found pattern at index i-j
                j = lps[j-1]
                
    return ret

T = input() # Text
P = input() # Pattern
lps = KMP(T, P)

print(len(lps))
print(*lps)
