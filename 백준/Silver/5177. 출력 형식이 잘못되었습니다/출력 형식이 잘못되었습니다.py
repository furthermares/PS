input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()

import re

def f(S):
    S = S.lower()
    S = " ".join(S.split())
    S = re.sub('\s*[({\[]\s*', '(', S)
    S = re.sub('\s*[)}\]]\s*', ')', S)
    S = re.sub('\s*,\s*', ';', S)
    S = re.sub('\s*;\s*', ';', S)
    S = re.sub('\s*\.\s*', '.', S)
    S = re.sub('\s*:\s*', ':', S)
    S = re.sub(' +', ' ', S)
    
    return S

for i in range(1,(K:=inp())+1):
    print(f"Data Set {i}: " + ("equal" if f(ins()) == f(ins()) else "not equal"))
    if not i == K: print()