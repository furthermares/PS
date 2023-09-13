input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

import re

slump = re.compile('([DE]F+)+G')

def is_slimp(S):
    if S == "AH":
        return True
    elif S.startswith("AB") and S.endswith("C"):
        return is_slimp(S[2:-1])
    elif S.startswith("A") and S.endswith("C"):
        return bool(slump.match(S[1:-1]))
    else:
        return False

for _ in range(inp()):       
    S = ins()

    ans = False
    if slump.search(S):
        s, e = list(slump.finditer(S))[-1].span()
        if e == len(S) and is_slimp(S[:s]):
            ans = True

    print("YES" if ans else "NO")